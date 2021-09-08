# python-objectively

this project uses init.py as the base class, the other classes / class files
are inherited by the init class so when init is instantiated init inherits
these methods/classes. init class can be expanded to include other classes the
init class is designed to be a minimal assortment of necessary system
functionality


this section of code is designed to cause all __init__
functions to be executed when init is instantiated

        classesTuple = Init.__mro__
        for className in classesTuple:
            m = re.match(r"^(.*)(['])(.*)(['])(.*)", str(className))           
            if m.group(3).strip() not in {'object'} and not re.search(r"^__main__", m.group(3).strip()) and not re.search(r"^init", m.group(3).strip()):
               file, cls = m.group(3).strip().split('.')
               instantiate=cls+'.__init__(self)'               
               eval(instantiate)
