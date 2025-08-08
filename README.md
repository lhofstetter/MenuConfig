# New Menuconfig (for Linux kernel)

This project is intended to offer a better alternative to the standard menuconfig
interface used when compiling the Linux kernel. While the ncurses-based interface works 
fine, it can be quite intimidating at first and is not the most visually attractive.

Additionally, navigation and ease of use are lacking, and require those using it to 
manually memorize paths to configuration options so that they can tweak the configuration
options they need.

This project intends to offer *substantial improvements* to the ncurses interface in the 
following key areas:
    - Navigation
    - Search
    - Build Automation
    - Item discovery

Currently, the project is using Textual to build a fully-featured TUI using Python. However,
depending on interest and availability, we may broaden our offerings to include web-based
UI's and other alternatives.
