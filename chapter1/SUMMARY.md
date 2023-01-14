## The Python Data Model

There's a difference between using `len(collection)` instead of `collection.len()`. \
Coming from another programming language the latter might make more sense. The former can and should be used because of something called the python data model.

The data model can be thought of as a description of Python as a framework: it formalizes the interfaces of the building blocks of the language itself.\
There are so called **special methods** that are being used to invoke the underlying functionalities, you have usually seen them already. They are always written with leading and trailing double underscores `__getitem__`.

[pythonic_card_deck.py](pythonic_card_deck.py) is an example that demonstrates the implementation of two special methods `__getitem__` and `__len__`
