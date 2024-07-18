from metagpt.actions import Action

class CheckCharacterAndFormat(Action):
    PROMPT_TEMPLATE: str = """
        Background:
            You are given a json text (```__json__```) which has two value characters and scenes.
            - characters: specifies an array where each entry is a dict. Consists of two fields, role_name is the character name, you can follow the story character name; personality represents the character's character qualities. 
            - Scene: Generate the main story of the corresponding scene, and generate scene characters with rich personality portraits. 

        Your tasks:
            1. make sure every character in the scenes should be found in the "characters" field. If not, please add that character in it.
            2. make sure the json text can be parse successfully by python json.load()
        Note, please do not give any explanation, you should output a plain json text.
    """

    name: str = "CheckCharacterAndFormat"

    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.replace("__json__", instruction)
        rsp = await self._aask(prompt)
        return rsp
