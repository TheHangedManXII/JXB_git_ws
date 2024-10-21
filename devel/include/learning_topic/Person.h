// Generated by gencpp from file learning_topic/Person.msg
// DO NOT EDIT!


#ifndef LEARNING_TOPIC_MESSAGE_PERSON_H
#define LEARNING_TOPIC_MESSAGE_PERSON_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace learning_topic
{
template <class ContainerAllocator>
struct Person_
{
  typedef Person_<ContainerAllocator> Type;

  Person_()
    : name()
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , r(0.0)
    , p(0.0)
    , w(0.0)  {
    }
  Person_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , r(0.0)
    , p(0.0)
    , w(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _name_type;
  _name_type name;

   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _z_type;
  _z_type z;

   typedef float _r_type;
  _r_type r;

   typedef float _p_type;
  _p_type p;

   typedef float _w_type;
  _w_type w;





  typedef boost::shared_ptr< ::learning_topic::Person_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::learning_topic::Person_<ContainerAllocator> const> ConstPtr;

}; // struct Person_

typedef ::learning_topic::Person_<std::allocator<void> > Person;

typedef boost::shared_ptr< ::learning_topic::Person > PersonPtr;
typedef boost::shared_ptr< ::learning_topic::Person const> PersonConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::learning_topic::Person_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::learning_topic::Person_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::learning_topic::Person_<ContainerAllocator1> & lhs, const ::learning_topic::Person_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.r == rhs.r &&
    lhs.p == rhs.p &&
    lhs.w == rhs.w;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::learning_topic::Person_<ContainerAllocator1> & lhs, const ::learning_topic::Person_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace learning_topic

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::learning_topic::Person_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::learning_topic::Person_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::learning_topic::Person_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::learning_topic::Person_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::learning_topic::Person_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::learning_topic::Person_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::learning_topic::Person_<ContainerAllocator> >
{
  static const char* value()
  {
    return "92cd5bc4b353da7d29b8bfedbb27bddb";
  }

  static const char* value(const ::learning_topic::Person_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x92cd5bc4b353da7dULL;
  static const uint64_t static_value2 = 0x29b8bfedbb27bddbULL;
};

template<class ContainerAllocator>
struct DataType< ::learning_topic::Person_<ContainerAllocator> >
{
  static const char* value()
  {
    return "learning_topic/Person";
  }

  static const char* value(const ::learning_topic::Person_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::learning_topic::Person_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n"
"float32  x\n"
"float32  y\n"
"float32  z\n"
"float32  r\n"
"float32  p\n"
"float32  w\n"
"\n"
;
  }

  static const char* value(const ::learning_topic::Person_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::learning_topic::Person_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.r);
      stream.next(m.p);
      stream.next(m.w);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Person_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::learning_topic::Person_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::learning_topic::Person_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.name);
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<float>::stream(s, indent + "  ", v.z);
    s << indent << "r: ";
    Printer<float>::stream(s, indent + "  ", v.r);
    s << indent << "p: ";
    Printer<float>::stream(s, indent + "  ", v.p);
    s << indent << "w: ";
    Printer<float>::stream(s, indent + "  ", v.w);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LEARNING_TOPIC_MESSAGE_PERSON_H