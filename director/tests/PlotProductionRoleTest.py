


# 可导入任何角色，初始化它，用一个开始的消息运行它，完成！
import asyncio

import os, sys
# 假设MetaGPT是你的项目根目录
project_root = "/Users/lion/Project/20240709sim/MetaGPT/"
if project_root not in sys.path:
    sys.path.append(project_root)
    

from metagpt.context import Context
from metagpt.logs import logger

from director.roles.PlotProductionRole import PlotProductionRole

async def main():
    context = Context()  # 显式创建会话Context对象，Role对象会隐式的自动将它共享给自己的Action对象
    role = PlotProductionRole(context=context)

    msg = '''
    {
        "scenes": [
            {
                "scene_name": "1",
                "main_plot": "Once upon a time, in a small village, there lived a beautiful maiden named Cinderella. She was kind and gentle, but her life was marked by hardship and sorrow.",
                "involve_characters": ["Cinderella"]
            },
            {
                "scene_name": "2",
                "main_plot": "Her mother had passed away when she was young, and her father had remarried soon after. Lady Tremaine treated Cinderella poorly, making her do all the household chores and forcing her to sleep in the attic.",
                "involve_characters": ["Cinderella", "Lady Tremaine"]
            },
            {
                "scene_name": "3",
                "main_plot": "One day, an invitation arrived from the King's palace, announcing a grand ball that would take place that evening. Lady Tremaine received the invitation and immediately began preparing for the occasion.",
                "involve_characters": ["Cinderella", "Lady Tremaine"]
            },
            {
                "scene_name": "4",
                "main_plot": "However, Cinderella was left out of the preparations and told to stay in her room. The mice friends, Jaq and Gus, saw how sad and disappointed Cinderella was becoming and decided to help her.",
                "involve_characters": ["Cinderella", "Jaq", "Gus"]
            },
            {
                "scene_name": "5",
                "main_plot": "They stole the stepsisters' beautiful gowns and brought them to Cinderella's attic, where they fit her perfectly. At the ball, Cinderella danced with Prince Charming and captivated him with her beauty and kindness.",
                "involve_characters": ["Cinderella", "Jaq", "Gus", "Prince Charming"]
            },
            {
                "scene_name": "6",
                "main_plot": "She left before midnight, leaving behind one of her glass slippers, which the Prince found. The Prince set out to find the mysterious girl whose foot fit the slipper.",
                "involve_characters": ["Cinderella", "Prince Charming"]
            },
            {
                "scene_name": "7",
                "main_plot": "He tried it on all of the maidens in the land, but none of them fit except for Cinderella. They got married and lived happily ever after.",
                "involve_characters": ["Cinderella", "Prince Charming"]
            }
        ]
    }
    '''

    msg = await role.run(msg.replace("\n", ""))
    logger.info(str(msg))

if __name__ == '__main__':
    asyncio.run(main())


