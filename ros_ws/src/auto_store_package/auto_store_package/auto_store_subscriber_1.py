import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import CompressedImage
import numpy as np
import cv2
from cv_bridge import CvBridge
from auto_store_package_msgs.msg import ImgNData
import base64

# 이미지 메시지 데이터를 어레이 형태로 변환
bridge = CvBridge() 

class ImageSubscriber(Node) :
  def __init__(self) :
    super().__init__('image_sub')
    qos = QoSProfile(depth=10)
    self.image_sub = self.create_subscription(
      ImgNData, # 임포트 된 메시지 타입 
      '/ImgNData', # 토픽리스트에서 조회한 토픽 주소
      self.callback, # 정의한 콜백함수
      qos)
    self.image = np.empty(shape=[1])

  def callback(self, msg) :
    img = np.reshape(np.array(msg.img_data), (320, 320, 3))

    if img is not None:
      cv2.imshow('ros_img_1', img)

    self.get_logger().info('data received : ' + msg.fruit_data)
    cv2.waitKey(10)
     
def main(args=None) :
  rclpy.init(args=args)
  node = ImageSubscriber()

  try :
    rclpy.spin(node)
  except KeyboardInterrupt :
    node.get_logger().info('Stopped by Keyboard')
  finally :
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__' :
  main()