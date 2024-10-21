#include "ros/ros.h"
#include "tf2_ros/static_transform_broadcaster.h"
#include "geometry_msgs/TransformStamped.h"   
#include "tf2/LinearMath/Quaternion.h"        //设置欧拉角
/* 
    静态坐标变换发布方:
        发布关于 laser 坐标系的位置信息 
    实现流程:
        1.包含头文件
        2.初始化 ROS 节点
        3.创建静态坐标转换广播器
        4.创建坐标系信息
        5.广播器发布坐标系信息
        6.spin()
*/
 
int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"static_pub");
    ros::NodeHandle nh;
    //3 创建静态坐标转换广播器
    tf2_ros::StaticTransformBroadcaster pub;
    //4 组织被发布的消息
    geometry_msgs::TransformStamped tfs;
    tfs.header.stamp =ros::Time::now();
    tfs.header.frame_id = "base_link"; //相对坐标系中被参考的那一个
    tfs.child_frame_id = "laser";
    tfs.transform.translation.x = 0.2;
    tfs.transform.translation.y = 0.0;
    tfs.transform.translation.z = 0.5;
    //需要根据欧拉角转换
    tf2::Quaternion qtn;//创建 四元数  对象
    //向该对象设置欧拉角，这个对象可以将欧拉角转换为四元数
    qtn.setRPY(0,0,0);//欧拉角的单位是弧度
    tfs.transform.rotation.x = qtn.getX();
    tfs.transform.rotation.y = qtn.getY();
    tfs.transform.rotation.z = qtn.getZ();
    tfs.transform.rotation.w = qtn.getW();
    //发布数据
    pub.sendTransform(tfs);
    ros::spin();
    return 0;
}