from metagpt.actions import Action
import json


        # { Test Input
        #     "scene_name": "2",
        #     "main_plot": "Her mother had passed away when she was young, and her father had remarried soon after. Lady Tremaine treated Cinderella poorly, making her do all the household chores and forcing her to sleep in the attic.",
        #     "involve_characters": ["Cinderella", "Lady Tremaine"]
        # }


class PlotGeneration(Action):
    PROMPT_TEMPLATE: str = """
        Background:
            You are now a plot generator: Given a text (```__json__```) which has two value characters and scenes.
            - characters: specifies an array where each entry is a dict. Consists of two fields, role_name is the character name, you can follow the story character name; personality represents the character's character qualities. 
            - Scene: Generate the main story of the corresponding scene, and generate scene characters with rich personality portraits. 

        Your tasks:
            1. You need to expand the details that may occur in the given scenario, including the main lines used to guide the story, the specific scenarios made up of dialogue and narrative, and the possible dialogue and behavioral interactions of the player.
            2. Narrator should only appear at the beginning and end of the story. 
            3. The "scene_name" in the output should be the same as the input. 
            4. Return a json text that can be parse successfully by python json.load()

        Output format: 
        ```
        {
            "scene_name": "3", 
            "conversations": [
                {
                    "speaker": "narrator",
                    "content": "Cinderella was in the kitchen, scrubbing the floor as the sun began to set. Lady Tremaine entered the room with a stern look on her face."
                },
                {
                    "speaker": "Lady Tremaine",
                    "content": "Cinderella! Why is this floor not spotless yet? You know how important tonight's dinner is."
                },
                {
                    "speaker": "Cinderella",
                    "content": "I'm sorry, stepmother. I'm doing my best. I'll make sure it's perfect."
                },
                {
                    "speaker": "Lady Tremaine",
                    "content": "Your best is never enough, Cinderella. After this, you need to prepare the dining room and polish the silverware."
                },
                {
                    "speaker": "Cinderella",
                    "content": "Yes, stepmother. I will get it done."
                },
                {
                    "speaker": "Lady Tremaine",
                    "content": "And don't forget to fetch fresh flowers for the centerpiece. The guests will be here soon, and everything must be perfect."
                },
                {
                    "speaker": "Cinderella",
                    "content": "Of course, stepmother. I'll go to the garden right after I finish here."
                },
                {
                    "speaker": "Lady Tremaine",
                    "content": "Good. See that you do. And remember, if anything goes wrong tonight, you'll be the one to blame."
                },
                {
                    "speaker": "Cinderella",
                    "content": "I understand. I'll make sure everything is just right."
                },
                {
                    "speaker": "narrator",
                    "content": "Lady Tremaine left the kitchen, leaving Cinderella to her work. Despite the harsh words, Cinderella remained determined to complete her tasks, hoping that one day her kindness and hard work would be rewarded."
                }
            ]
        }
        ```
        Note, please do not give any explanation, you should output a plain json text.
    """

    name: str = "PlotGeneration"

    async def run(self, instruction: str):
        instruction_json = json.loads(instruction)
        conversations = {
            "conversations": []
        }
        for scene in instruction_json["scenes"]:
            scene_str = json.dumps(scene)
            prompt = self.PROMPT_TEMPLATE.replace("__json__", scene_str)
            rsp = await self._aask(prompt)
            conversations["conversations"].append(rsp)

        return json.dumps(conversations)
