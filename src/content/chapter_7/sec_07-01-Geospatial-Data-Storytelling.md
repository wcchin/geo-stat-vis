# 7.1 Designing the story before designing the map

A data story needs more than an attractive opening and a list of results. It needs a reader, a question worth following, and a sequence in which each view changes what the reader understands. Narrative visualisation research describes a balance between the flow directed by the author and the discoveries available to the reader [1]. In a teaching book, we can guide the first reading while leaving room for students to inspect alternative measures afterwards.

## A creative brief grounded in evidence

Begin with a short brief. Its purpose is to focus decisions, including decisions about what to leave out. For this example, the central idea is **“Define convenience before comparing places.”** That is narrower and more defensible than “We found Singapore’s best neighbourhood.” It gives each subsequent view a job.

| Design question | Working answer for our example |
|---|---|
| Audience | A student or household trying to interpret neighbourhood information |
| Human concern | “I want daily life to be manageable, but maps offer several incompatible measures.” This is our proposed concern, to be tested with readers. |
| Familiar assumption | More nearby bus stops may look like better transport access. Treat this as an opening hypothesis, not a belief held by everyone. |
| Evidence-based tension | Two selected blocks have equal nearby stop counts but very different recorded boarding activity. Neither quantity measures a complete journey. |
| Central idea | Convenience needs an explicit definition; different spatial measures support different claims. |
| Reader payoff | The reader can ask what was counted, within what boundary, during what period, and for which need. |
| Next action | Inspect the evidence and specify an additional measure before making a neighbourhood comparison. |

The tension should be found in checked results. Our analysis did not require a predetermined “hidden truth” about expensive and inexpensive neighbourhoods. If the layers had aligned closely, the story could instead explain where they agree and why that agreement still does not demonstrate causation.

## From analysis order to reading order

We prepared coordinates, checked missing values, calculated distances, selected cases and compared summaries. Readers do not need to encounter every processing operation in that order. They need enough context to understand each claim when it appears. Technical details remain available in the methods and reproducibility package.

Our six-frame sequence starts with a recognisable question and ends with a revised way of asking it:

| Frame | Reader's question | Evidence or visual | What this frame should achieve |
|---|---|---|---|
| 1. The invitation | “What makes a neighbourhood convenient?” | A short audience scenario and the three evidence layers | Establish relevance without promising an answer the data cannot provide |
| 2. The price view | “What do these homes actually sell for?” | Selling-block median prices, with transaction counts | Introduce observed prices and the limits of this sale sample |
| 3. The transport view | “Does nearby mean well connected?” | Equal-radius bus-stop counts beside nearby boarding activity | Separate proximity and activity from complete accessibility |
| 4. The local view | “Convenient for what?” | Hawker, school and park reference points in three local maps | Show why amenity categories and geometry matter |
| 5. The challenge | “Would another boundary change the picture?” | 500 m versus 800 m counts | Make a consequential analytical choice visible |
| 6. The payoff | “What should I ask before deciding?” | A short evidence ledger and missing-data statement | Leave the reader with a usable evaluation habit |

Notice that the story does not finish with a winning town. Its resolution is a change in understanding. The opening word “convenient” sounded like a single property. By the end, the reader can see that it depends on needs, measures and boundaries. That intellectual payoff can be engaging without a sensational conclusion.

## From visual thinking to a communication plan: OTAS

Chapter 1 introduces the course guideline **Observe, Think, Assess, Show**. Here we use it to plan and revise the neighbourhood example. OTAS is a flexible teaching guideline, rather than a named research framework or a rule that every project must follow in one order. The creative brief identifies the audience and purpose; the guideline helps connect exploratory work with the eventual story.

**Observe.** Read the metadata and inspect both source records and initial displays. In the neighbourhood example, check what a selling block, a bus stop and a park reference point represent. Compare distributions and local contexts before choosing a headline. Record the selection and temporal coverage with each provisional view.

**Think.** Write down possible interpretations and alternatives. Equal nearby stop counts may suggest similar provision, while boarding activity raises another question about use. List the further evidence needed to compare service quality or accessibility. The aim is to develop explanations worth checking, rather than infer causes directly from a striking map.

**Assess.** Check identifiers, joins, units, coordinate systems, denominators and case selection. Test whether another radius or price measure changes the comparison. Use relevant literature to examine possible mechanisms and contrary evidence. A successful check increases support for a specific claim; it does not verify every explanation that could be attached to the display. If a check exposes a problem, return to the observations or reconsider the question.

**Show.** Choose the views and sequence that help the intended reader inspect the supported interpretation. Decide how to arrange panels, label units, use colour and type, and state the source and limits. Show a draft to a reader and ask what they think it claims. Their answer may reveal a need to revise the analysis, wording or hierarchy. The map-components and hierarchy sections develop these design decisions in detail.

The loop is useful because exploratory discoveries and presentation choices influence each other. A new question can lead to another observation, a sensitivity check can reshape the central idea, and reader feedback can expose an ambiguity. Keep those returns possible while making the final reading path clear.

## Selecting examples without selecting the answer

For the local comparison, we fixed three illustrative towns—Bishan, Tampines and Woodlands—before examining their amenity results. Within each town, we selected the block with at least three sample transactions whose median resale price was closest to the town's transaction median. Alphabetical address order breaks a tie. Each selected block happens to have five transactions.

This transparent rule avoids hand-picking a block because its POI pattern makes a dramatic map. It does not make the three blocks statistically representative of their towns. A town transaction median also weights blocks with more transactions more heavily. We therefore name the block in each panel and describe the results as local illustrations.

**Try it.** Rewrite the six-frame sequence for a transport planner. Which frame would you replace with service frequency or journey-time evidence? Explain why a new audience changes the required data as well as the wording.

