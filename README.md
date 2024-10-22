## 开源代码与组件使用情况说明：

机械臂使用57、42、20型号步进电机驱动，Arduino mega2560单片机以及pc端作为主控单元。软体伸缩插管作为末端执行单元
### 作品安装说明：
### 一、系统运行环境说明：
<table align="center" border="1">
    <tr>
        <th align="center">名称</th>  
        <th align="center">版本号</th>
        <th align="center">备注</th>
    </tr>
    <tr>
        <th align="center">操作系统		</th>  
        <th align="center">Ubuntu18.04</th>
        <th align="center">64位</th>
    </tr>
    <tr>
        <td rowspan="3">开发环境</td>
        <td>ROS1</td>
        <td rowspan="3">无</td>
    </tr>
    <tr>
        <td>Python3.8</td>
    </tr>
    <tr>
        <td>Opencv4.6.0</td>
    </tr>
</table>

### 二、系统运行环境搭建：
<strong>1、ROS1系统的安装</strong>

以下均在终端中执行：
<pre>
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo rosdep init
rosdep update
</pre>
<strong>2、创建工作空间：</strong>
<pre>
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws/
catkin_make
</pre>
此时可在文件管理器中看到我们创建的工作空间catkin_ws

<strong>3、安装python3.8</strong>
<pre>
sudo apt-get update 
sudo apt-get install python3.6
</pre>
<strong>4、安装opencv4.6.0</strong>
<pre>
sudo apt update
sudo apt upgrade
pip3 install opencv-python
</pre>

<strong>5、安装并编译功能包</strong>
将附件提供的功能包解压在工作空间catkin_ws中的src文件夹中，打开终端输入
<pre>
cd ~/catkin_ws
catkin_make --cmake-args             -DCMAKE_BUILD_TYPE=Release             -DPYTHON_EXECUTABLE=/usr/bin/python3             -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m             -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so
</pre>

在终端运行
<pre>
	roslaunch smallArmRobot_moveit_config demo.launch
</pre>

可实现在rviz仿真界面中对人体咽喉部位的位置发布，从而可通过ros中的话题订阅功能实现机械人与人体咽喉部位的相对位置确定。后运行
<pre>
	rosrun smallArmRobot_driver moveit_i_demo1.py
</pre>	
	
 可调用moveit实现对机械臂运行到人体咽喉部位的模拟仿真效果，并实现路径规划，从而能被现实中吸痰机械臂调用规划路径实现位置移动。

