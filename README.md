# 🎬 CODE-TYPER - Realistic Code Typing Simulator

> **Make Your Coding Videos Look Professional with AI-Like Typing**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Perfect for YouTube tutorials, coding demonstrations, and educational videos. CODE-TYPER simulates realistic human typing with natural delays, occasional typos, and thinking pauses.

![Status](https://img.shields.io/badge/Status-Production_Ready-success)

---

## 🌟 Why CODE-TYPER?

Ever tried recording a coding tutorial and struggled with:
- ❌ Typing too fast or making mistakes
- ❌ Forgetting what to say while typing
- ❌ Having to re-record segments
- ❌ Code not fitting in the frame
- ❌ Maintaining consistent typing speed

**CODE-TYPER solves ALL of these!**

✅ Pre-write your code, record your voice separately  
✅ Perfect, consistent typing every time  
✅ Realistic human-like delays and occasional typos  
✅ Focus on explaining, not typing  
✅ Professional-looking videos with minimal effort  

---

## ⚡ Key Features

### 🎯 **Realistic Typing Simulation**
- Variable typing speed (20-200 WPM)
- Random delays that mimic human thinking
- Optional typos with auto-correction
- Pauses at punctuation and code blocks

### 🎮 **Easy to Use**
- Simple GUI interface
- Load any code file (.ino, .py, .cpp, etc.)
- Global hotkeys work even when minimized
- 5-second countdown before typing starts

### 🎨 **Customizable**
- Adjust typing speed (WPM)
- Control error rate (0-10%)
- Enable/disable realistic pauses
- Works with ANY text editor or IDE

### 🔥 **Perfect For**
- YouTube coding tutorials
- Educational demos
- Live coding presentations
- Twitch streaming
- Screen recordings

---

## 📦 Installation

### Quick Install

```bash
git clone https://github.com/OrbitScript/code-typer.git
cd code-typer
pip install -r requirements.txt
```

### Requirements
- Python 3.7+
- Windows, macOS, or Linux

### Dependencies
```bash
pip install pyautogui pillow
```

---

## 🎮 How to Use

### Step 1: Launch CODE-TYPER
```bash
python code_typer.py
```

### Step 2: Load Your Code
- Click **"📂 Load File"** to load any code file
- Or paste your code directly in the text area
- Supports `.ino`, `.py`, `.cpp`, `.js`, and more!

### Step 3: Configure Settings
- **Typing Speed**: 20-200 WPM (default: 80 WPM)
- **Error Rate**: 0-10% chance of typos (default: 2%)
- **Realistic Pauses**: Adds natural thinking delays

### Step 4: Start Recording
1. Open your video recording software (OBS, ScreenFlow, etc.)
2. Click on Arduino IDE (or any editor)
3. Press **F9** in CODE-TYPER
4. You have 5 seconds to switch to your editor!
5. Watch the magic happen ✨

### Global Hotkeys
- **F9** - Start typing (5 second delay)
- **F10** - Pause/Resume
- **F11** - Stop

---

## 🎬 Perfect Workflow for Videos

### Traditional Method (Hard)
1. Write code while recording
2. Explain what you're doing
3. Make mistakes, re-record
4. Edit out pauses and errors
5. Frustrated and time-consuming ❌

### CODE-TYPER Method (Easy)
1. Write your code beforehand
2. Start CODE-TYPER with hotkey
3. Record yourself explaining pre-typed code
4. Perfect typing + perfect explanation
5. Professional result in one take ✅

---

## 📊 Example Use Cases

### 🎓 **YouTube Tutorial Creator**
```
Problem: Need to type code while explaining concepts
Solution: Pre-write code, use CODE-TYPER, focus on explanation
Result: Professional, polished tutorials
```

### 💼 **Live Coding Presenter**
```
Problem: Audience waiting while you type
Solution: Load code, trigger with F9, present smoothly
Result: Engaging presentations without dead air
```

### 📺 **Twitch Coder**
```
Problem: Chat moves too fast while coding
Solution: Pre-code complex parts, interact with chat
Result: Better engagement, fewer mistakes
```

---

## ⚙️ Advanced Settings

### Typing Speed Guide
| WPM | Description | Best For |
|-----|-------------|----------|
| 20-40 | Very slow | Absolute beginners |
| 40-60 | Beginner | Learning tutorials |
| 60-80 | **Average** | Most tutorials |
| 80-120 | Fast | Advanced demos |
| 120-200 | Very fast | Speed coding |

### Error Rate Guide
| % | Description | Effect |
|---|-------------|--------|
| 0% | Perfect | No typos (looks robotic) |
| 2% | **Realistic** | Occasional typo + fix |
| 5% | Human-like | More natural mistakes |
| 10% | Beginner | Frequent corrections |

---

## 🎯 Pro Tips

### For Best Results:

1. **Pre-test Your Code**
   - Make sure it compiles/runs
   - No syntax errors
   - Properly formatted

2. **Adjust Speed for Content**
   - Slower for complex code
   - Faster for simple examples
   - Match your speaking pace

3. **Use Realistic Pauses**
   - Mimics thinking time
   - Natural-looking
   - Better for learning videos

4. **Practice the Hotkeys**
   - F9 to start
   - F10 to pause (fix mistakes)
   - F11 to stop

5. **Window Management**
   - Position IDE where you want it
   - Ensure cursor is in editor
   - Test before recording

---

## 🖥️ Compatible Editors

CODE-TYPER works with ANY text editor or IDE:

✅ Arduino IDE  
✅ VS Code  
✅ Sublime Text  
✅ Notepad++  
✅ PyCharm  
✅ Atom  
✅ Vim/Emacs  
✅ Notepad  
✅ Any text input field  

---

## 🛠️ Technical Details

### How It Works
1. Reads your code from file or text input
2. Calculates typing delays based on WPM setting
3. Uses PyAutoGUI to simulate keypresses
4. Adds random variations for realism
5. Optional typos with backspace correction
6. Smart pausing at code blocks

### Safety Features
- 5-second countdown before starting
- Pause/resume functionality
- Emergency stop (F11)
- Works in background (global hotkeys)

### Performance
- Low CPU usage
- Works with any screen resolution
- No dependencies on specific IDEs
- Cross-platform compatibility

---

## 📸 Screenshots

### Main Interface
```
╔══════════════════════════════════════════╗
║         🎬 CODE-TYPER v1.0.0            ║
║   Realistic Code Typing Simulator       ║
╚══════════════════════════════════════════╝

📝 Your Code to Type
┌─────────────────────────────────────────┐
│ // Your code appears here               │
│ void setup() {                          │
│   pinMode(13, OUTPUT);                  │
│ }                                       │
└─────────────────────────────────────────┘

⚙️ Settings
Typing Speed: [80] WPM
Error Rate: [2] %
☑ Realistic Pauses

🎮 Controls
[▶️ START (F9)] [⏸️ PAUSE (F10)] [⏹️ STOP (F11)]
```

---

## 🎥 Video Recording Tips

### OBS Studio Setup
1. Start OBS recording
2. Open Arduino IDE in frame
3. Launch CODE-TYPER
4. Press F9 when ready
5. Focus returns to IDE automatically

### Screen Recording Best Practices
- Use 1080p or higher resolution
- Increase IDE font size (14-18pt)
- Use high-contrast theme
- Position IDE prominently
- Test typing speed beforehand

---

## 🔧 Troubleshooting

### Issue: Typing Too Fast
**Solution**: Lower WPM in settings (try 60-80)

### Issue: Not Typing in Correct Window
**Solution**: Click on editor AFTER pressing F9, during 5-sec countdown

### Issue: Hotkeys Not Working
**Solution**: Make sure CODE-TYPER window is open (can be minimized)

### Issue: Random Characters
**Solution**: Disable special keyboard software or language inputs

### Issue: Skipping Characters
**Solution**: Increase typing delay, close resource-heavy programs

---

## 🚀 Future Features (Roadmap)

- [ ] Syntax highlighting preview
- [ ] Custom hotkey configuration
- [ ] Speed ramping (start slow, speed up)
- [ ] Sound effects (keyboard clicks)
- [ ] Cursor position saving
- [ ] Multiple code snippets queue
- [ ] Export typing as video overlay
- [ ] Web-based version
- [ ] Mobile app companion

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m "✨ Add amazing feature"`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

Feel free to use CODE-TYPER in your videos! Attribution appreciated but not required.

---

## 🙏 Acknowledgments

- Built with [PyAutoGUI](https://pyautogui.readthedocs.io/)
- Inspired by the need for better coding tutorial tools
- Thanks to the YouTube creator community

---

## 💬 Support & Community

- 🐛 Found a bug? [Open an issue](https://github.com/OrbitScript/code-typer/issues)
- 💡 Have an idea? [Start a discussion](https://github.com/OrbitScript/code-typer/discussions)
- 📧 Email: support@orbitscript.dev

---

## 🎬 Made a Video Using CODE-TYPER?

Tag us on social media!
- Twitter: @OrbitScript
- YouTube: OrbitScript
- Instagram: @orbitscript

We'd love to feature your content! 🌟

---

<div align="center">

**Made with ❤️ for Content Creators**

[![GitHub](https://img.shields.io/badge/GitHub-OrbitScript-181717?logo=github)](https://github.com/OrbitScript)
[![YouTube](https://img.shields.io/badge/YouTube-OrbitScript-red?logo=youtube)](https://youtube.com/@OrbitScript)

**Star this repo if it helped you! ⭐**

</div>
