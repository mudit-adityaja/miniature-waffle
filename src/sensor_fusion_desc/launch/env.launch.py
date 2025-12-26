from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg = FindPackageShare('sensor_fusion_desc')

    world = PathJoinSubstitution([pkg, 'worlds', 'turtlebot3_house.world'])
    models = PathJoinSubstitution([pkg, 'models'])
    worlds = PathJoinSubstitution([pkg, 'worlds'])

    gz_launch = PathJoinSubstitution(
        [FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py']
    )

    return LaunchDescription([
        SetEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH',
            [models, TextSubstitution(text=':'), worlds]
        ),
        SetEnvironmentVariable(
            'IGN_GAZEBO_RESOURCE_PATH',
            [models, TextSubstitution(text=':'), worlds]
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch),
            launch_arguments={
                'gz_args': world,
                'on_exit_shutdown': 'True',
            }.items(),
        ),
    ])
