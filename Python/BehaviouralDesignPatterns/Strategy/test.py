from shareStrategy import EmailStrategy, SlackStrategy
from application import CameraPlusApplication, BasicCameraApplication


slack_share_strategy = SlackStrategy()
email_share_strategy = EmailStrategy()

basic_camera_application = BasicCameraApplication(shareStrategy= email_share_strategy)
basic_camera_application.edit()
basic_camera_application.share()

basic_camera_application.setShareStrategy(shareStrategy= slack_share_strategy)
basic_camera_application.share()