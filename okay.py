{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'array' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-fc0c9b575654>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0marray\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'array' is not defined"
     ]
    }
   ],
   "source": [
    "n = array([2,3,4,5,6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'n' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-349653be3a92>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'n' is not defined"
     ]
    }
   ],
   "source": [
    "print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{2, 3, 4, 5, 6}\n"
     ]
    }
   ],
   "source": [
    "from numpy import*\n",
    "n=array({2,3,4,5,6})\n",
    "print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from win32com.client import Dispatch\n",
    "def speak(str):\n",
    "    speak = Dispatch(\"SAPI.SpVoice\")\n",
    "    speak.Speak(str)\n",
    "\n",
    "\n",
    "if __name__=='__main__':\n",
    "    speak(\"hey \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "Could not find PyAudio; check installation",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python38\\site-packages\\speech_recognition\\__init__.py\u001b[0m in \u001b[0;36mget_pyaudio\u001b[1;34m()\u001b[0m\n\u001b[0;32m    107\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 108\u001b[1;33m             \u001b[1;32mimport\u001b[0m \u001b[0mpyaudio\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    109\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mImportError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pyaudio'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-8371f4e39b6b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0msr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mMicrophone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msource\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"speak anything:\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[0maudio\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlisten\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msource\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python38\\site-packages\\speech_recognition\\__init__.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, device_index, sample_rate, chunk_size)\u001b[0m\n\u001b[0;32m     77\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     78\u001b[0m         \u001b[1;31m# set up PyAudio\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 79\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyaudio_module\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_pyaudio\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     80\u001b[0m         \u001b[0maudio\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyaudio_module\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mPyAudio\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     81\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python38\\site-packages\\speech_recognition\\__init__.py\u001b[0m in \u001b[0;36mget_pyaudio\u001b[1;34m()\u001b[0m\n\u001b[0;32m    108\u001b[0m             \u001b[1;32mimport\u001b[0m \u001b[0mpyaudio\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    109\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mImportError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 110\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Could not find PyAudio; check installation\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    111\u001b[0m         \u001b[1;32mfrom\u001b[0m \u001b[0mdistutils\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mversion\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    112\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpyaudio\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__version__\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"0.2.11\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: Could not find PyAudio; check installation"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "r = sr.Recognizer()\n",
    "\n",
    "\n",
    "with sr.Microphone() as source:\n",
    "    print(\"speak anything:\")\n",
    "    audio = r.listen(source)\n",
    "\n",
    "    try:\n",
    "        text = r.recognize_google(audio)\n",
    "        print(\"you said : {}\".format(text))\n",
    "\n",
    "    except:\n",
    "        print('sorry')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
