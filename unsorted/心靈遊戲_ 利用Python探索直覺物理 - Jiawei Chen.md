# 心靈遊戲: 利用Python探索直覺物理 - Jiawei Chen

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}
~~心靈遊戲~~ -> 心智遊戲

 安裝所需的package: `pip install pybullet opencv-python baselines` 

bullet是個物理引擎，可以拿來當作train model用的模擬環境：
https://github.com/bulletphysics/bullet3

## [URDF (Unified Robot Description Format)](http://wiki.ros.org/urdf)
- 用來描述機器人的結構，例如關節、link（連接兩關節的東西）之類的參數
- 線上 URDF viewer http://www.mymodelrobot.appspot.com/
- 要玩 pybullet 至少要懂 URDF
- [範例](https://github.com/bulletphysics/bullet3/blob/master/examples/pybullet/examples/humanoid_manual_control.py)
- 真實機械手臂 URDF: [kuka](https://github.com/ros-industrial/kuka_experimental)
- [SolidWork URDF Plugin](http://wiki.ros.org/sw_urdf_exporter)
- Blender 可以用[Phobos](https://github.com/rock-simulation/phobos)導出URDF
- [Free 3D](https://free3d.com/)

## Reinforcement Learning
- [Open AI Gym](https://gym.openai.com/)
- [Baseline](https://github.com/openai/baselines ): 現成的reinforement learning演算法: 
    - pybullet已整合 
    - train_cartpole: [openAI version](https://github.com/openai/baselines/blob/master/baselines/deepq/experiments/train_cartpole.py), [pybullet version](https://github.com/bulletphysics/bullet3/blob/master/examples/pybullet/gym/pybullet_envs/baselines/train_pybullet_cartpole.py)
- Self-Supervised Damage-Avoiding Manipulation Strategy Optimization via Mental Simulation: [ArXiv](https://arxiv.org/abs/1712.07452), [Video](http://robotics.jacobs-university.de/TMP/jint_manipulation_strategy_optimization.mp4)

- GIBSON虛擬環境 http://gibsonenv.stanford.edu/
- 用 [Meshlab](http://www.meshlab.net/) 將 3D point cloud (.ply) 轉 mesh (.obj)
- 用手機、kinect來把真實世界掃成模型 xhttp://introlab.github.io/rtabmap/

###### tags: `pycontw2018`
