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
    channel_type =  LaunchConfiguration('channel_type', default='serial')
    serial_port = LaunchConfiguration('serial_port', default='/dev/ttyUSB0')
    serial_port2 = LaunchConfiguration('serial_port', default='/dev/ttyUSB1')
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='460800')
    frame_id = LaunchConfiguration('frame_id', default='laser_frame')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')
    scan_mode = LaunchConfiguration('scan_mode', default='Standard')
    topic_name = LaunchConfiguration('topic_name', default='scan1')
    topic_name2 = LaunchConfiguration('topic_name', default='scan2')
    flip_x_axis = LaunchConfiguration('flip_x_axis', default='false')

    

    

    lidar1 = Node(
        package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            parameters=[{'channel_type':channel_type,
                         'serial_port': serial_port,
                         'serial_baudrate': serial_baudrate,
                         'frame_id': frame_id,
                         'inverted': inverted,
                         'angle_compensate': angle_compensate,
                         'scan_mode': scan_mode,
                         'topic_name': topic_name,
                         'flip_x_axis': flip_x_axis}],
            output='screen')

    lidar2 = Node(
        package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            parameters=[{'channel_type':channel_type,
                            'serial_port': serial_port2,
                            'serial_baudrate': serial_baudrate,
                            'frame_id': frame_id,
                            'inverted': inverted,
                            'angle_compensate': angle_compensate,
                            'scan_mode': scan_mode,
                            'topic_name': topic_name2,
                            'flip_x_axis': flip_x_axis}],
            output='screen')
    

    return LaunchDescription([
        lidar1,
        lidar2
    ])

