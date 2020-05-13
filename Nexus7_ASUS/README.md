# Purpose
How to Unlock Nexus7_ASUS  

# Table of Contents  
[Unlocking the Nexus 7 (2013) Bootloader](#unlocking-the-nexus-7-2013-bootloader)  

# Unlocking the Nexus 7 (2013) Bootloader  
[Unlocking the Nexus 7 (2013) Bootloader 26th July, 2013](https://forum.xda-developers.com/showthread.php?t=2379618)  

1. Install the Android SDK (and Google USB driver).
    1. [Android SDK](http://developer.android.com/sdk/index.html)
    2. [Google USB Driver (Windows)](http://developer.android.com/sdk/win-usb.html)
2. Enable USB debugging on the Nexus 7.
    1. Unlock Developer Options by going to Settings > About Tablet and clicking on the build number seven times.
    2. Go to Settings > Developer Options and check USB debugging. Click OK on the warning.
3. Connect the Nexus 7 via USB and reboot the Nexus 7 into the bootloader.
    Note: Users have reported failures and "Access is Denied" errors when connected via USB 3.0 ports so use USB 1.1 or 2.0 to be on the safe side.
    1. Open a command line / terminal and navigate to your SDK platform-tools directory.
    2. Enter
        Code:
        ```
        adb reboot bootloader
        ```
        and hit enter.
4. Once the Nexus 7 boots to the bootloader, unlock it
    1. At the command line / terminal enter
        Code:
        ```
        fastboot oem unlock
        ```
        and press enter.
    2. On the Nexus 7, use the volume up button to select 'Yes' on the 'Unlock bootloader?' screen.
    3. Press the power button to save your choice and verify on the next screen that you see 'LOCK STATE - UNLOCKED' at the bottom.
    4. Use your volume keys to select 'Start' and click the power button to factory reset and reboot.
5. Enjoy your unlocked bootloader!

```

```

# Troubleshooting


# Reference


* []()
![alt tag]()

# h1 size

## h2 size

### h3 size

#### h4 size

##### h5 size

*strong*strong  
**strong**strong  

> quote  
> quote

- [ ] checklist1
- [x] checklist2

* 1
* 2
* 3

- 1
- 2
- 3
