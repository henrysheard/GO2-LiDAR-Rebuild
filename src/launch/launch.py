import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():


   # Path to the config file
   config_file = os.path.join(
       get_package_share_directory('slam'),
       'config',
       'mapper_params_online_async.yaml'
   )


   return LaunchDescription([


       # SLAM Toolbox Node (Async Mode)
       Node(
           package='slam_toolbox',
           executable='async_slam_toolbox_node',
           name='slam_toolbox',
           output='screen',
           parameters=[config_file]
       )
   ])
