from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="openpose_ros2",
            node_executable="openpose_ros2",
            node_name="openpose_node",
            output="screen",
            parameters=[
                {
                    "is_debug_mode": False,
                    "openpose_root": "/home/vlad/openpose",
                    "is_image_compressed": False,
                    "image_node": "/camera/color/image_raw",
                    "show_video_steam": True
                }
            ]
        )
    ])
