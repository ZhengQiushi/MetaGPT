from metagpt.actions import Action
from metagpt.logs import logger

class SceneExtraction(Action):
    PROMPT_TEMPLATE: str = """
        You are now a professional scene extractor: given a story (__topic__), you need to break it down into a series of characters and scenes from God's point of view. 
        - characters: specifies an array where each entry is a dict. Consists of two fields, role_name is the character name, you can follow the story character name; personality represents the character's character qualities. It is recommended to contain no more than 50 words 
        - Scene: Generate the main story of the corresponding scene, and generate scene characters with rich personality portraits. 
        The output should be a json in the following format:
        {
        "characters": [
            {
                "role_name": "和尚1",
                "personality": "自私"
            }, 
            {
                "role_name": "和尚2",
                "personality": "自私, 懒惰"
            }, 
            {
                "role_name": "和尚3",
                "personality": "自私, 懒惰, 虔诚"
            }, 
        ]
        "scenes": [
            {
                "scene_name": "1",
                "main_plot": "以前山庙里有个和尚1。他每天一个人挑一担水生活，给菩萨案桌上的水瓶添水、念经、敲木鱼，生活过得很安逸。",
                "involve_characters": ["和尚1"]
            },
            {
                "scene_name": "2",
                "main_plot": "后来庙里来了位和尚2。他一到庙里，就把半缸水喝光了。 和尚1叫他去挑水，和尚2心想一个人去挑水太吃亏了 ，便要和尚1和他一起去抬水，两个人只能抬一只桶，而且水桶必须放在担子的中央，两人才心安理得。这样总算还有水喝。",
                "involve_characters": ["和尚1", "和尚2"]
            },            
            {
                "scene_name": "3",
                "main_plot": "后来，又来了个和尚3。他也想喝水，但缸里没水。和尚1和和尚2 叫新来的 和尚3 自己去挑，新来的和尚3挑来一担水，立刻独自喝光了。从此谁也不挑水，三个和尚就没水喝。大家各念各的经，各敲各的木鱼，菩萨面前的净水瓶也没人添水，花草枯萎了。",
                "involve_characters": ["和尚1", "和尚2", "和尚3"]
            },
            {
                "scene_name": "4",
                "main_plot": "夜里老鼠出来偷东西，谁也不管。结果老鼠路过烛台，打翻烛台，燃起大火。三个和尚这才一起奋力救火 ，大火扑灭了，他们也觉醒了。从此三个和尚齐心协力，水自然就更多了。",
                "involve_characters": ["和尚1", "和尚2", "和尚3"]
            },
        ]
        }

        Note, please do not give any explanation, you should output a plain json text.
    """

    name: str = "SceneExtraction"

    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.replace("__topic__", instruction)

        rsp = await self._aask(prompt)
        logger.info(self.name, ":" , str(rsp))
        return rsp
