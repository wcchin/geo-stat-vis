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

## Selecting examples without selecting the answer

For the local comparison, we fixed three illustrative towns—Bishan, Tampines and Woodlands—before examining their amenity results. Within each town, we selected the block with at least three sample transactions whose median resale price was closest to the town's transaction median. Alphabetical address order breaks a tie. Each selected block happens to have five transactions.

This transparent rule avoids hand-picking a block because its POI pattern makes a dramatic map. It does not make the three blocks statistically representative of their towns. A town transaction median also weights blocks with more transactions more heavily. We therefore name the block in each panel and describe the results as local illustrations.

**Try it.** Rewrite the six-frame sequence for a transport planner. Which frame would you replace with service frequency or journey-time evidence? Explain why a new audience changes the required data as well as the wording.
