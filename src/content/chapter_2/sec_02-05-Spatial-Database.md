# 2.5 Spatial database

**Reading route.** Follow the station keys, the two endpoint joins, the duplication counterexample and the spatial join first. Database administration and indexing provide optional background after those operations are clear.

The previous sections treated a prepared column as something we could summarise, transform and classify. But real analysis usually combines several sources. Station codes and names belong in one table, exit locations in another, and repeated activity observations in others. A database organises these relationships so that we can retrieve the information needed for a question without confusing the entities or repeatedly maintaining the same attributes.

Our MRT example makes this concrete. To label an OD observation, we need station information twice: once for the origin and once for the destination. To attach a planning-area label, we need coordinates and polygons. The first operation matches identifiers; the second matches geometries.

## Tables, keys and relationships

A relational database stores information in related tables. A primary key uniquely identifies a row and cannot be null. A foreign key refers to an identifying key in another table. A composite key uses several fields together. In our station lookup, `station_code` identifies one selected station complex. In the OD table, both endpoint codes refer to that lookup, while the complete observation key also includes month, day type, hour and transport type.

| Relationship | MRT example | Consequence |
|---|---|---|
| One-to-one | A station and one deliberately selected reference-point record | A valid join can attach geometry without multiplying station rows |
| One-to-many | A station and its exit-location records | One station can match several exits |
| Many-to-one | Many OD observations matched to an origin-station lookup | The right-hand station key must be unique to preserve OD rows |
| Many-to-many | Stations related to other stations through directed OD observations | Store the relationship explicitly, with its temporal context and trip count |

Cardinality describes the relationship being modelled, not a promise made by the word “join.” Optionality matters too: a station might lack a matching location in a snapshot. A foreign-key constraint in a database can prevent some unmatched identifiers, while a CSV or in-memory table needs explicit checks. Constraints do not establish that an identifier names the correct real-world object.

## Store each fact where it belongs

Repeating a station name and every exit coordinate in every monthly OD record creates redundant information and opportunities for inconsistent updates. A practical design keeps station attributes, exits, OD observations and station activity separate. Queries connect them when needed.

This illustrates database normalisation: organise attributes according to their dependencies to reduce update, insertion and deletion anomalies. A station name depends on a station identifier, not on which destination appears in an OD row. Formal normal forms are more precise than simply saying “one table per object”; the useful habit here is to identify which key each fact depends on.

A combined identifier such as `NS17/CC15` is treated as one source key for a station complex in this demonstration. If line membership becomes analytically relevant, create a separate relation linking the complex to line-specific codes. Do not split the OD fact into repeated copies of its trip count.

::::{dropdown} Go deeper: what a DBMS adds

A database management system (DBMS) provides storage and operations such as create, read, update and delete, along with mechanisms for constraints, concurrent access, transactions and recovery. These capabilities depend on the system and its configuration; a database does not automatically guarantee data accuracy or security. PostgreSQL with PostGIS is one spatial-capable option. A desktop GIS or notebook can also perform the small joins here without requiring students to administer a server.

::::

## Join the station lookup twice

For the observation `NS17/CC15 → CC16`, the reported count is 256. Matching the origin supplies “Bishan”; matching the destination supplies “Marymount.” Use role-specific field names so the result remains unambiguous.

```{figure} ../datasets/mrt_data_foundations_202609/figures/02_two_joins.svg
:label: ch2-two-endpoint-joins
:alt: A single OD record receives its origin and destination names through two many-to-one matches to the same station lookup.

One lookup plays two roles. Attaching names preserves the observation and its count; it does not create another trip.
```

The following pandas example uses the field names in the bundled CSVs:

```python
origin = stations[["station_code", "station_name"]].rename(columns={
    "station_code": "ORIGIN_PT_CODE", "station_name": "origin_name"
})
destination = stations[["station_code", "station_name"]].rename(columns={
    "station_code": "DESTINATION_PT_CODE", "station_name": "destination_name"
})
joined = od.merge(origin, on="ORIGIN_PT_CODE", how="left",
                  validate="many_to_one")
joined = joined.merge(destination, on="DESTINATION_PT_CODE", how="left",
                      validate="many_to_one")
assert len(joined) == len(od)
assert joined["TOTAL_TRIPS"].sum() == od["TOTAL_TRIPS"].sum()
assert joined[["origin_name", "destination_name"]].notna().all().all()
```

Here, `od` is the 12-row slice and `stations` is the four-row lookup. Both endpoint codes must be non-missing and the lookup keys unique. A left join retains the selected observations so unmatched names remain inspectable; an inner join would exclude unmatched observations. An outer join can help inspect keys appearing on only one side. Null-key behaviour also differs between tools: pandas can match null join keys to each other, whereas ordinary SQL equality does not, so validate keys before relying on a cross-tool result.

The checked result has 12 rows and 12,904 trips before and after both matches, with no missing names. These checks support this small lookup; they do not establish full-network matching coverage.

## A successful command can still produce the wrong unit

Bishan has five exit records in our source snapshot. Joining every OD record directly to all exits of its origin repeats that record once per matching exit. Across the four stations, the 12 OD observations expand to **57 rows**. Summing the repeated counts gives **78,396**, rather than 12,904. The extra count was created by duplication, not transport activity.

This is not a reason to prohibit one-to-many joins. They are useful when the intended result is one row per matching exit. It is a reason to state the output unit and avoid summing station-level facts after expansion. If the goal is to attach a station-level exit count, aggregate exits first. If the goal is one reference geometry, select that geometry explicitly. If the goal is to inspect related exits interactively, a GIS relationship or “relate” can expose them without flattening all records into one observation table.

A join need not create a permanently stored combined table. It can be a query or view, or it can be materialised as a snapshot. Whether updates propagate depends on implementation; “join” does not by itself mean static, and “relate” does not guarantee real-time synchronisation.

## Match geography with a spatial join

A spatial join attaches attributes according to a geometric relationship, such as containment, intersection, a distance threshold or nearest feature. For our containment example, we test each selected station reference point against URA planning-area polygons. Station names are not the matching key.

```{figure} ../datasets/mrt_data_foundations_202609/figures/03_spatial_join.svg
:label: ch2-spatial-join
:alt: Schematic of the calculated reference-point matches: Bishan and Marymount in Bishan planning area, Serangoon in Serangoon, and Paya Lebar in Geylang.

The point-in-polygon labels come from real source coordinates and URA boundaries. The drawing's shapes and positions are illustrative, not a geographical map. Each point represents the selected source exit, not the full station complex.
```

| Selected station reference | Source exit | Covering planning area |
|---|---|---|
| Bishan | Exit A | Bishan |
| Serangoon | Exit A | Serangoon |
| Paya Lebar | Exit A | Geylang |
| Marymount | Exit A | Bishan |

Paya Lebar station's selected reference falls in Geylang planning area. Matching the strings “Paya Lebar” in the two tables would not answer the containment question. Similarly, grouping the four results gives two selected reference points in Bishan, one in Serangoon and one in Geylang. These are subset counts, not totals for all stations or estimates of passengers residing in each area.

Choose the spatial predicate deliberately. A boundary-inclusive rule equivalent to `ST_Covers(polygon, point)` accepts points on a polygon boundary; strict point `within` excludes them. A point on a shared boundary can therefore receive two covering matches. Our four reference points each receive exactly one match. All 19 selected exits happen to have the same area label as their respective reference point in this snapshot, but that should not be assumed for every station.

An illustrative PostGIS query, assuming compatible geometry columns and valid polygons, is:

```sql
SELECT s.station_code, s.station_name, a.planning_area
FROM stations AS s
LEFT JOIN planning_areas AS a
  ON ST_Covers(a.geom, s.geom);
```

This query is a schema illustration, not a command to run against unimported CSVs: `stations.geom` must first be constructed from the chosen longitude/latitude fields with the correct CRS, and `planning_areas.geom` must contain the area polygons. A left spatial join can return more than one output row per station, so check match counts as well as unmatched rows.

## Coordinates, distance and spatial indexes

Containment here uses compatible EPSG:4326 points and polygons and does not calculate distances. For a metre-based proximity question, transform the geometries to a suitable projected CRS such as EPSG:3414 and state the distance operation. Relabelling an EPSG:4326 geometry as EPSG:3414 does not perform that transformation. A straight-line radius also differs from a walking-network distance or travel time.

::::{dropdown} Go deeper: spatial indexes and implementation references

Spatial indexes speed up searching by organising spatial extents or locations. An R-tree-style index can identify candidate features using bounding rectangles, after which the exact spatial predicate checks the geometry. A rectangle match alone need not establish containment or intersection of the original shapes. Point-oriented k-d trees, quadtrees and bounding-box indexes support different structures and queries; their internal algorithms are beyond this chapter's requirements.

An index affects how efficiently candidates are found, not which real-world representation is appropriate. Faster querying cannot repair a wrong coordinate system, repeated observations or a poorly chosen reference point. See the [PostGIS spatial-query documentation](https://postgis.net/docs/using_postgis_query.html) and [`ST_Covers` definition](https://postgis.net/docs/ST_Covers.html) for the implemented operations; the [pandas merge guide](https://pandas.pydata.org/docs/user_guide/merging.html) explains tabular join validation.

::::

## From prepared data to defensible analysis

Before proceeding, be able to state the observation unit, temporal scope, identifiers, geometry representation, missing-data treatment and consequences of every join. These decisions determine which distributions and patterns are meaningful to analyse. A spatially explicit table is not automatically an analytically appropriate one; it becomes useful when its construction matches the intended question.

The [offline reproduction package](../datasets/mrt_data_foundations_202609/README.md) checks both endpoint joins, totals, the unsafe-join counterexample and the reference-point matches. Chapter 3 builds on these foundations by examining what statistical comparisons can tell us—and what their assumptions require.

**Self-check:** Why not assign the station's full activity to every exit and sum by area?

```{dropdown} Feedback
The station activity does not identify which exit each trip used. Copying the total to every exit repeats it. An allocation requires additional observations or a justified model; an ordinary join supplies neither.
```
