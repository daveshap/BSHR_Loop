# demo01

## Contributors
@daveshap  @samgriek

## Setup
Create a .env file in the same location as the example.env by compying it.

```bash
cd demo01/src && cp example.env .env
```

Set the open api key

```bash
OPENAI_API_KEY="<your_openai_api_key_here>"
```

## Install dependencies
Use pip or other package manager tool to install the dependencies in the requirements.txt file.

```bash
pip install -r requirements.txt
```

## Start the demo
The entry point for the demo is the main.py file.  If you are using VSCode you can just click the main file and issue a `CTRL + F5` key combination command.

Type your question at the command prompt and press `Enter` to continue.

## Enjoy
It is worth experimenting by adding additional features.  See some example results below...

## Example

### Total Tokens
20062

### User Query
What is at the bottom of the deepest part of the deepest ocean?

### Final Hypothesis
"The deepest part of the ocean is the Challenger Deep, located in the Mariana Trench in the western Pacific Ocean. The depth of the Challenger Deep is approximately 10,920 ± 10 m, but the exact geodetic location and depth are not definitively established due to the challenges of deep-sea exploration. The Challenger Deep is named after the British Royal Navy survey ships HMS Challenger (1872–1876) and HMS Challenger II (1950-1952). \n\nThe first descent to the Challenger Deep was made by the bathyscaphe Trieste in January 1960, and since then, a total of twenty-seven people have descended to this depth as of July 2022. Notably, the Limiting Factor, a deep-submergence vehicle (DSV) manufactured by Triton Submarines and owned by Gabe Newell's Inkfish, has made multiple descents to the Challenger Deep. This vehicle, commissioned by Victor Vescovo for $37 million, holds records for the deepest crewed dives in all five oceans and is certified for full ocean depth dives.\n\nThe bottom of the Challenger Deep, like other deep-sea environments, is characterized by extreme pressure, low temperatures, and complete darkness. Despite these harsh conditions, life has been found at these depths, demonstrating the adaptability of life on Earth. The seafloor is mostly covered in marine sediment, which originates from various sources including soil, rocks, marine organisms, chemical precipitation, underwater volcanoes, and meteorite debris. The composition of this sediment is highly variable and can range in thickness from a few millimeters to tens of kilometers. This sediment provides a habitat for marine life, especially microorganisms, and contains fossilized remains that can provide information on past climates, plate tectonics, ocean circulation, and major extinctions.\n\nHowever, our understanding of the deep-sea environment and the life it supports is still limited due to the difficulties and challenges associated with deep-sea exploration. As such, the bottom of the deepest part of the ocean remains a largely unexplored and mysterious place."

### Satisficed
`True`

### Feedback
"The final hypothesis is comprehensive and well-structured, covering the key aspects of the user's query. It provides detailed information about the deepest part of the ocean, the Challenger Deep, including its location, depth, and history of exploration. It also discusses the conditions at the bottom of the ocean, the composition of the sediment, and the life forms that inhabit these extreme environments. The hypothesis also acknowledges the challenges and limitations of deep-sea exploration, which is an important aspect of the user's query. The search queries were well-targeted and the results provided relevant and detailed information that was used effectively in the final hypothesis. Therefore, the information need has been satisficed."