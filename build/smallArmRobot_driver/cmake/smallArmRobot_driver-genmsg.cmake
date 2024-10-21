# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "smallArmRobot_driver: 1 messages, 0 services")

set(MSG_I_FLAGS "-IsmallArmRobot_driver:/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg;-IsmallArmRobot_driver:/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(smallArmRobot_driver_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg" NAME_WE)
add_custom_target(_smallArmRobot_driver_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "smallArmRobot_driver" "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(smallArmRobot_driver
  "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/smallArmRobot_driver
)

### Generating Services

### Generating Module File
_generate_module_cpp(smallArmRobot_driver
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/smallArmRobot_driver
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(smallArmRobot_driver_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(smallArmRobot_driver_generate_messages smallArmRobot_driver_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg" NAME_WE)
add_dependencies(smallArmRobot_driver_generate_messages_cpp _smallArmRobot_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(smallArmRobot_driver_gencpp)
add_dependencies(smallArmRobot_driver_gencpp smallArmRobot_driver_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS smallArmRobot_driver_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(smallArmRobot_driver
  "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/smallArmRobot_driver
)

### Generating Services

### Generating Module File
_generate_module_eus(smallArmRobot_driver
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/smallArmRobot_driver
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(smallArmRobot_driver_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(smallArmRobot_driver_generate_messages smallArmRobot_driver_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg" NAME_WE)
add_dependencies(smallArmRobot_driver_generate_messages_eus _smallArmRobot_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(smallArmRobot_driver_geneus)
add_dependencies(smallArmRobot_driver_geneus smallArmRobot_driver_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS smallArmRobot_driver_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(smallArmRobot_driver
  "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/smallArmRobot_driver
)

### Generating Services

### Generating Module File
_generate_module_lisp(smallArmRobot_driver
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/smallArmRobot_driver
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(smallArmRobot_driver_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(smallArmRobot_driver_generate_messages smallArmRobot_driver_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg" NAME_WE)
add_dependencies(smallArmRobot_driver_generate_messages_lisp _smallArmRobot_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(smallArmRobot_driver_genlisp)
add_dependencies(smallArmRobot_driver_genlisp smallArmRobot_driver_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS smallArmRobot_driver_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(smallArmRobot_driver
  "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/smallArmRobot_driver
)

### Generating Services

### Generating Module File
_generate_module_nodejs(smallArmRobot_driver
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/smallArmRobot_driver
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(smallArmRobot_driver_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(smallArmRobot_driver_generate_messages smallArmRobot_driver_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg" NAME_WE)
add_dependencies(smallArmRobot_driver_generate_messages_nodejs _smallArmRobot_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(smallArmRobot_driver_gennodejs)
add_dependencies(smallArmRobot_driver_gennodejs smallArmRobot_driver_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS smallArmRobot_driver_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(smallArmRobot_driver
  "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/smallArmRobot_driver
)

### Generating Services

### Generating Module File
_generate_module_py(smallArmRobot_driver
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/smallArmRobot_driver
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(smallArmRobot_driver_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(smallArmRobot_driver_generate_messages smallArmRobot_driver_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sdfg/JXB_git_ws/src/smallArmRobot_driver/msg/step_msg.msg" NAME_WE)
add_dependencies(smallArmRobot_driver_generate_messages_py _smallArmRobot_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(smallArmRobot_driver_genpy)
add_dependencies(smallArmRobot_driver_genpy smallArmRobot_driver_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS smallArmRobot_driver_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/smallArmRobot_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/smallArmRobot_driver
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET smallArmRobot_driver_generate_messages_cpp)
  add_dependencies(smallArmRobot_driver_generate_messages_cpp smallArmRobot_driver_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(smallArmRobot_driver_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/smallArmRobot_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/smallArmRobot_driver
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET smallArmRobot_driver_generate_messages_eus)
  add_dependencies(smallArmRobot_driver_generate_messages_eus smallArmRobot_driver_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(smallArmRobot_driver_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/smallArmRobot_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/smallArmRobot_driver
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET smallArmRobot_driver_generate_messages_lisp)
  add_dependencies(smallArmRobot_driver_generate_messages_lisp smallArmRobot_driver_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(smallArmRobot_driver_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/smallArmRobot_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/smallArmRobot_driver
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET smallArmRobot_driver_generate_messages_nodejs)
  add_dependencies(smallArmRobot_driver_generate_messages_nodejs smallArmRobot_driver_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(smallArmRobot_driver_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/smallArmRobot_driver)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/smallArmRobot_driver\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/smallArmRobot_driver
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET smallArmRobot_driver_generate_messages_py)
  add_dependencies(smallArmRobot_driver_generate_messages_py smallArmRobot_driver_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(smallArmRobot_driver_generate_messages_py std_msgs_generate_messages_py)
endif()
