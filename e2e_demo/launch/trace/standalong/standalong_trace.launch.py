import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from tracetools_launch.action import Trace


def generate_launch_description():
    period1_ns = int(1.0/11.0*1.0e9)
    period2_ns = int(1.0/7.0*1.0e9)
    timer_period_ns = int(1.0/3.0*1.0e9)
    callback_duration_ns = int(0.01*1.0e9)

    return launch.LaunchDescription([
        Trace(
            session_name='standalong_demo',
            events_kernel=[]
        )
    ])
