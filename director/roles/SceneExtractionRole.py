from metagpt.roles import Role

import asyncio
import re
import subprocess

import fire

from metagpt.actions import Action
from metagpt.logs import logger
from metagpt.roles.role import Role, RoleReactMode
from metagpt.schema import Message

from actions.SceneExtraction import SceneExtraction
from actions.GetMainStory import GetMainStory
from actions.CheckCharacterAndFormat import CheckCharacterAndFormat

class SceneExtractionRole(Role):
    name: str = "Alice"
    profile: str = "SceneExtractionRole"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([GetMainStory, SceneExtraction, CheckCharacterAndFormat])
        self._set_react_mode(react_mode="by_order")

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        # By choosing the Action by order under the hood
        # todo will be first SimpleWriteCode() then SimpleRunCode()
        todo = self.rc.todo

        msg = self.get_memories(k=1)[0]  # find the most k recent messages
        result = await todo.run(msg.content)
        
        logger.info(self.name, ":" , str(result))

        msg = Message(content=result, role=self.profile, cause_by=type(todo))

        self.rc.memory.add(msg)
        return msg