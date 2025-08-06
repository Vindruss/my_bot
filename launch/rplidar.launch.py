import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='sllidar_ros',
            executable='sllidar_c1_launch.py',
            output='screen',
            parameters=[{
                'frame_id': 'laser_frame'
            }]
        )
    ])
