{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "TclError",
     "evalue": "bitmap \"C:\\Users\\mayank\\Desktop\\Python Project\\instagram.ico\" not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTclError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-184f4af1920f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtkinter\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mtk\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mwin\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtk\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mTk\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mwin\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miconbitmap\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mr'C:\\Users\\mayank\\Desktop\\Python Project\\instagram.ico'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mwin\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Instagram\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\tkinter\\__init__.py\u001b[0m in \u001b[0;36mwm_iconbitmap\u001b[1;34m(self, bitmap, default)\u001b[0m\n\u001b[0;32m   1869\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtk\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcall\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'wm'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'iconbitmap'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_w\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'-default'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1870\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1871\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtk\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcall\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'wm'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'iconbitmap'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_w\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbitmap\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1872\u001b[0m     \u001b[0miconbitmap\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mwm_iconbitmap\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1873\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mwm_iconify\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTclError\u001b[0m: bitmap \"C:\\Users\\mayank\\Desktop\\Python Project\\instagram.ico\" not defined"
     ]
    }
   ],
   "source": [
    "import tkinter as tk\n",
    "win = tk.Tk()\n",
    "win.iconbitmap(r'C:\\Users\\mayank\\Desktop\\Python Project\\instagram.ico')\n",
    "win.title(\"Instagram\")\n",
    "\n",
    "win.mainloop()"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
