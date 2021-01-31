#-------------------------------------------------------------------------
#
#  objects sample1 - pass base class methods to any user defined class
#
#--------------------------------------------------------------------------

import pprint

class Base ():

  def __init__(self, trace):
      self.trace_mode = trace

  def  _add(self, object, name, value):
      if name in object:
         print ('instance variable: ' + name + ' exists')
         return
      else:
         self._trace('added instance variable ' + name)
         object[name] = value

  def  _get(self, object, name):
      if name in object:
          return object[name]
      else:
          print('instance variable: ' + name + ' not instantiated')


  def  _set(self, object, name, value):
      if name in object:
          object[name] = value
      else:
          print('instance variable: ' + name + ' not instantiated')
          return

  def  _trace(self, text):
      if self.trace_mode == 'trace':
         print ('\t[trace]: ' + text)

  def  _new(self,name,type):
      instance = {'name':name, 'type':type}
      return instance



class Programmer(Base):
  programmers = 0

  def __init__(self, trace):
      self.trace_mode = trace


  def _set_trace_mode(self, trace):
      self.trace_mode = trace

  @classmethod
  def describePosition(cls, position):
      if position == '__PROGRAMMER__':
         description =  position + ' : ' + 'a software developer who codes business logic in a high level programming language'
         return (description)


#------------------------------------------------
#                   M A I N
#------------------------------------------------
pp = pprint.PrettyPrinter(indent=4)

object = Programmer('no-trace')
node0 = object._new('__PROGRAMMER__','python')

pp.pprint(object.__dict__)
object._add(node0, 'gender', None)
object._set(node0, 'gender','female')
pp.pprint (  object._get(node0, 'gender'))
pp.pprint(node0)

node1 = object._new('__PROGRAMMER__','C')
object._set_trace_mode('trace')
object._add(node1, 'gender', 'male')

pp.pprint( Programmer.describePosition('__PROGRAMMER__'))
pp.pprint(object.__dict__)


