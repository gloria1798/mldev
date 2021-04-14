from typing import Any, Callable, Dict, Sequence, Tuple, Union
import torch

SequenceOrTensor = Union[Sequence, torch.Tensor]


def greeting(name: str) -> str:
    return 'Hello ' + name


def register(callback):
    name = input("   what is your name: ")
    print(callback(name))


def regis(myfunc: Callable[[int], str]) -> None:
    name = input("what is your name: ")
    print(myfunc(name))

# regis(greeting)


def foo(x: Union[str, int]):
    print(x)


foo(5.01)
