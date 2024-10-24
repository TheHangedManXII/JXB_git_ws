

#include "ros/ros.h"
#include <vector>
#include "tf2_ros/static_transform_broadcaster.h"
#include "geometry_msgs/TransformStamped.h"
#include "tf2/LinearMath/Quaternion.h"
 
 
int main(int argc, char** argv)
{
    ros::init(argc, argv, "ik_test_node");
    ros::NodeHandle n;
    tf2_ros::StaticTransformBroadcaster broadcaster;
    geometry_msgs::TransformStamped ts;
    ts.header.seq=100;
    ts.header.stamp=ros::Time::now();
    ts.header.frame_id="base_link";
    ts.child_frame_id="laser";
    ts.transform.translation.x=0.0;
    ts.transform.translation.y=0.0;
    ts.transform.translation.z=0.0;
    ts.transform.rotation.x=0;
    ts.transform.rotation.y=0;
    ts.transform.rotation.z=0;
    ROS_INFO("nihao woshi :%lf",ts.transform.rotation.x);
    tf2::Quaternion qtn;
    qtn.setRPY(0,0,0);
    ts.transform.rotation.x=qtn.getX();
    ts.transform.rotation.y=qtn.getY();
    ts.transform.rotation.z=qtn.getZ();
    ts.transform.rotation.w=qtn.getW();
 
    broadcaster.sendTransform(ts);
    ros::spin();
}
