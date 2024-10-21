#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include "math.h"    //常数 M_PI = π; M_PI/2 = π/2;
 
int main(int argc, char** argv)
{
    ros::init(argc, argv, "tf_publisher");//初始化ROS节点与节点名称
    ros::NodeHandle n;                    //创建节点的句柄
    ros::Rate loop_rate(100);             //控制节点运行的频率,与loop.sleep共同使用
 
    tf::TransformBroadcaster broadcaster; //创建一个TransformBroadcaster对象(tf广播器,)，是用来发布tf变换树;
    
    tf::Transform base2laser;             //激光雷达坐标系LiDAR_link;创建一个Transform对象,用于描述两个坐标系之间的转化关系，即两个点的相对坐标;
    tf::Quaternion q;                     //Quaternion应为四元数；
    q.setRPY(M_PI,M_PI*0.9,M_PI*1.5);              //setRPY应为欧拉角,设置旋转坐标
    base2laser.setRotation(q);                   
    base2laser.setOrigin(tf::Vector3(0,1.1,1.5));//setOrigin应为平移坐标,设平移坐标，laser2在base的(1.1,0,1.5)位置
 
    tf::Transform base3laser;             //相机坐标系Cam_link
    tf::Quaternion p;
    p.setRPY(M_PI/2,0,M_PI);                 //设置旋转坐标
    base3laser.setRotation(p);              
    base3laser.setOrigin(tf::Vector3(0,0.8,1.1));//设平移坐标，laser3在base的(0.8,0,1.1)位置
 
    tf::Transform base4laser;
    tf::Quaternion rs;
    rs.setRPY(0,M_PI,0);                   //设置旋转坐标
    base4laser.setRotation(rs);              
    base4laser.setOrigin(tf::Vector3(0,0,0));//设平移坐标，laser4在base的(1,0,0)位置
 
 
    while (n.ok())
    {
        //循环发布坐标变换，两种方式
        broadcaster.sendTransform(tf::StampedTransform(base2laser,ros::Time::now(),"link2","LiDAR_link"));
	broadcaster.sendTransform(tf::StampedTransform(base3laser,ros::Time::now(),"link2","Cam_link"));
	broadcaster.sendTransform(tf::StampedTransform(base4laser,ros::Time::now(),"link2","IMU_link"));
	//发布tf变换树的类型，一个变换树包含 变换、时间戳、父坐标系frame_id、子坐标系frame_id；
	//tf::StampedTransform(transform, ros::Time::now(), “turtle1”, “carrot1”)
        //broadcaster.sendTransform(tf::StampedTransform(tf::Transform(tf::Quaternion(0, 0, 0, 0), tf::Vector3(1, 0.0, 0)),ros::Time::now(),"base_link", "base_laser"));
        loop_rate.sleep();
    }
    return 0;
}
 