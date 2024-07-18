from metagpt.actions import Action
from metagpt.logs import logger

class GetMainStory(Action):
    PROMPT_TEMPLATE: str = """
        Do you know the story of __topic__? Please tell me the details of the story at least 200 words. 
        Note, please do not make any explanation, you should output a plain text.
    """

    name: str = "GetMainStory"

    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.replace("__topic__", instruction)

        rsp = await self._aask(prompt)
        logger.info(self.name, ":" , str(rsp))
        return rsp
