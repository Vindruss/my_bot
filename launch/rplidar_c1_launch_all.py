#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import time


def generate_launch_description():

    lidar1 = Node(
        package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            parameters=[{'channel_type':'serial',
                         'serial_port': '/dev/ttyUSB0',
                         'serial_baudrate': '460800',
                         'frame_id': 'laser_frame',
                         'inverted': 'false',
                         'angle_compensate': 'true',
                         'scan_mode': 'Standard',
                         'topic_name': 'scan1',
                         'flip_x_axis': 'false'}],
            output='screen')

    lidar2 = Node(
        package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            parameters=[{'channel_type':'serial,
                         'serial_port': '/dev/ttyUSB1',
                         'serial_baudrate': '460800',
                         'frame_id': 'laser_frame',
                         'inverted': 'false',
                         'angle_compensate': 'true',
                         'scan_mode': 'Standard',
                         'topic_name': 'scan2',
                         'flip_x_axis': 'false'}],
            output='screen')
    

    return LaunchDescription([
        lidar1,
        lidar2
    ])

