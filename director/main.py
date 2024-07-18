# 可导入任何角色，初始化它，用一个开始的消息运行它，完成！
import asyncio

import os, sys
# 假设MetaGPT是你的项目根目录
project_root = "/Users/lion/Project/20240709sim/MetaGPT/"
if project_root not in sys.path:
    sys.path.append(project_root)
    

from metagpt.context import Context
from metagpt.logs import logger

from roles.SceneExtractionRole import SceneExtractionRole

async def main():
    msg = "the Grimms' Fairy Tales: Cinderella"
    context = Context()  # 显式创建会话Context对象，Role对象会隐式的自动将它共享给自己的Action对象
    role = SceneExtractionRole(context=context)
    msg = await role.run(msg)
    logger.info(str(msg))

if __name__ == '__main__':
    asyncio.run(main())