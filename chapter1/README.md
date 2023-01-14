## The Python Data Model

There's a difference between using `len(collection)` instead of `collection.len()`. \
Coming from another programming language the latter might make more sense. The former can and should be used because of something called the python data model.

The data model can be thought of as a description of Python as a framework: it formalizes the interfaces of the building blocks of the language itself.\
There are so called **special methods** that are being used to invoke the underlying functionalities, you have usually seen them already. They are always written with leading and trailing double underscores `__getitem__`.

- [pythonic_card_deck.py](pythonic_card_deck.py) is an example that demonstrates the implementation of two special methods `__getitem__` and `__len__` 
- [vector.py](vector.py) implements a few more of these special methods and function overloading, in addition, I added typehints to get used to them.


## short summary
By implementing special methods, our objest can behave like built-in types. \
Basic requirements for Python objects are to provide usable string representation of itself. This is especially helpful when we need to debug or log functions. This is why special methods `__repr__` and `__str__` exist in the Data Model.

The use and implementation of the majority of remaining special methods in the Python data model are going to be part of what is being discussed in this book. (=