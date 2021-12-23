{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "PriorityQueue",
      "provenance": [],
      "authorship_tag": "ABX9TyMI+txyHhXl/XthT1EWedXZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jiheey/DataStructure-Python/blob/main/PriorityQueue.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "AT5xZ9kx467h"
      },
      "outputs": [],
      "source": [
        "class PriorityQueue:\n",
        "\n",
        "\tdef __init__(self):\n",
        "\t\tself.items = []\n",
        "\n",
        "\tdef isEmpty(self):\n",
        "\t\treturn len(self.items)==0 \n",
        "\n",
        "\tdef size(self): return len(self.items) \n",
        "\n",
        "\tdef clear(self): return self.items=[]\n",
        "\n",
        "\tdef enqueue(self, item):\n",
        "\t\tself.items.append(item)\n",
        "\n",
        "\tdef findMaxIndex(self):\n",
        "\t\tif self.isEmpty(): return None\n",
        "\t\telse: \n",
        "\t\t\thighest=0\n",
        "\t\t\tfor i in range(1, self.size()):\n",
        "\t\t\t\tif self.items[1] > self.items[highest]:\n",
        "\t\t\t\t\thighest = i \n",
        "\t\t\t\treturn highest\n",
        "\n",
        "\tdef dequeue(self):\n",
        "\t\thighest = self.findMaxIndex()\n",
        "\t\tif highest is not None:\n",
        "\t\t\treturn self.items.pop(highest)\n",
        "\n",
        "\tdef peek(self): \n",
        "\t\thighest = findMaxIndex()\n",
        "\t\tif highest is not None: \n",
        "\t\t\treturn self.items[highest]"
      ]
    }
  ]
}