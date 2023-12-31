# deeplearning-repo-3

# 딥러닝 기반의 무인 매장 시스템
## 📖 프로젝트 개요
### Action recognition 기반으로 어떤 과일을 샀는지 인식하면 DB 및 PyQt를 이용하여 해당 물건을 자동으로 결제
### Yolov8 기반 Object counting을 활용하여 매대별 과일 종류 및 개수 파악


## 🥇 시스템 구성
<p align="center">
  <img src="https://github.com/addinedu-ros-3rd/iot-repo-2/assets/61872888/de7222e0-8f16-41d1-b555-d392aa396d1d" width="80%" style="float:left">
</p>


## 👨‍👧‍👦 팀원 및 역할
|이름|역할|
|------|------|
|강한얼|객체 인식 모델 YOLOv8 학습, 딥러닝 기반 고객 행동 인식 모델 학습, 중앙 시스템 Main 함수 설계, 시스템 구성도/ Use case/ Sequence diagram 제작|
|김준표|딥러닝 기반 고객 행동 인식 모델 학습 및 Test(Rule-based), 시스템 하드웨어 구성도 제작(일부), roslibpy 기반 영상 이미지 통신 및 PyQt 출력(일부)|
|조태상|매대의 과일 종류별 수량 인식 딥러닝 모델(일부), 시스템 데이터 저장을 위한 DB 개발, 관리자 시스템 GUI 개발
|조홍기|매대의 과일 종류별 수량 인식 딥러닝 모델 개발(전체), 무인 매장 시스템 - 중앙 관리 시스템간 통신 모듈 개발|
|최규호|시스템 데이터 저장을 위한 DB 개발|


## 📆 프로젝트 기간
### 2023.11.16~2023.12.15


## 🎯 기술 스택



|      |      |
|------|------|
|개발 환경|<img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white">, <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white">, <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=OpenCV&logoColor=white">|
|언어|<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">|
|DB|<img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">, <img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=for-the-badge&logo=Amazon RDS&logoColor=white">|
|GUI|<img src="https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=Qt&logoColor=white">|
|통신|<img src="https://img.shields.io/badge/ROS-22314E?style=for-the-badge&logo=ROS&logoColor=white">|


## 🥇 프로젝트 소개 
### - USE CASE Diagram
<p align="center">
  <img src="https://github.com/haneol0415/calculator/assets/61872888/4819b346-45ac-46a7-9ddc-0a321045a179" width="90%" style="float:left">
</p>


### - Sequence Diagram
<p align="center">
  <img src="https://github.com/addinedu-ros-3rd/iot-repo-2/assets/61872888/a4fd1508-cc41-45e2-bbb0-19b58027f95b" width="90%" style="float:left">
</p>



## 🖌️ GUI
![image](https://github.com/addinedu-ros-3rd/deeplearning-repo-3/assets/87626122/7fb4d54b-dad2-4dfa-b5d4-e06d7ecf25a7)


## 🏅 DBMS 구성도
![dl_db_result drawio (3)](https://github.com/addinedu-ros-3rd/deeplearning-repo-3/assets/104709955/e9949bd6-afa5-4538-bbf2-fa8c182fc87b)


## 🏁 발표 자료 링크
https://docs.google.com/presentation/d/1L9lDK6GptjHDVC1pk5et46PFg5JRmc-w_r4A61HhIeM/edit#slide=id.g263d5bba2a3_0_5


## 개발 환경 설정



> Main 시스템
Ubuntu 22.04
ROS2 Humble
    1. install ros2 humble
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
    2. sudo apt-get install ros-humble-rosbridge-server
    3. cd ros_ws
    4. source /opt/ros/humble/setup.bash
    5. colcon build
    6. source install/local_setup.bash
    7. cmd 1 -> ros2 launch rosbridge_server rosbridge_websocket_launch.xml
    8. cmd 2 -> ros2 run auto_store_package auto_store_subscriber


> 전체 python requirements
    numpy
    opencv-python
    roslibpy
    torch
    mysql-connector-python
    PyQt5==5.14.2
    PyQt5-sip
