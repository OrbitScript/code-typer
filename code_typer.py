#!/usr/bin/env python3
"""
CODE-TYPER - Realistic Code Typing Simulator for Videos
Automatically types your code with realistic human-like delays
Perfect for YouTube tutorials and demonstrations
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyautogui
import time
import random
import threading
import json
from pathlib import Path

class CodeTyper:
    """Main application for realistic code typing simulation"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 CODE-TYPER v1.0.0 - Realistic Code Typing Simulator")
        self.root.geometry("900x700")
        self.root.configure(bg='#1e1e1e')
        
        # State variables
        self.code_content = ""
        self.is_typing = False
        self.typing_thread = None
        self.pause_event = threading.Event()
        self.pause_event.set()  # Initially not paused
        
        # Settings
        self.settings = {
            'typing_speed': 80,  # WPM
            'error_rate': 2,     # % chance of typo
            'pause_on_newline': True,
            'delay_after_line': 0.5,
            'delay_after_block': 1.0,
            'realistic_pauses': True
        }
        
        self.setup_ui()
        self.setup_hotkeys()
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # Header
        header = tk.Frame(self.root, bg='#2d2d30', height=60)
        header.pack(fill='x', padx=0, pady=0)
        
        title = tk.Label(
            header, 
            text="🎬 CODE-TYPER",
            font=('Arial', 24, 'bold'),
            bg='#2d2d30',
            fg='#61dafb'
        )
        title.pack(pady=10)
        
        subtitle = tk.Label(
            header,
            text="Realistic Code Typing for Video Recording",
            font=('Arial', 10),
            bg='#2d2d30',
            fg='#cccccc'
        )
        subtitle.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Code input section
        code_frame = tk.LabelFrame(
            main_frame,
            text="📝 Your Code to Type",
            font=('Arial', 11, 'bold'),
            bg='#252526',
            fg='#ffffff',
            bd=2
        )
        code_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        # Text area with scrollbar
        text_container = tk.Frame(code_frame, bg='#1e1e1e')
        text_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(text_container)
        scrollbar.pack(side='right', fill='y')
        
        self.code_text = tk.Text(
            text_container,
            font=('Consolas', 11),
            bg='#1e1e1e',
            fg='#d4d4d4',
            insertbackground='white',
            yscrollcommand=scrollbar.set,
            wrap='none',
            padx=10,
            pady=10
        )
        self.code_text.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.code_text.yview)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#1e1e1e')
        button_frame.pack(fill='x', pady=(0, 10))
        
        # Load file button
        self.load_btn = tk.Button(
            button_frame,
            text="📂 Load File",
            command=self.load_file,
            bg='#0e639c',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=8,
            relief='flat',
            cursor='hand2'
        )
        self.load_btn.pack(side='left', padx=5)
        
        # Clear button
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_code,
            bg='#d13438',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=8,
            relief='flat',
            cursor='hand2'
        )
        self.clear_btn.pack(side='left', padx=5)
        
        # Settings section
        settings_frame = tk.LabelFrame(
            main_frame,
            text="⚙️ Settings",
            font=('Arial', 11, 'bold'),
            bg='#252526',
            fg='#ffffff',
            bd=2
        )
        settings_frame.pack(fill='x', pady=(0, 10))
        
        settings_inner = tk.Frame(settings_frame, bg='#252526')
        settings_inner.pack(fill='x', padx=10, pady=10)
        
        # Typing speed
        speed_frame = tk.Frame(settings_inner, bg='#252526')
        speed_frame.pack(fill='x', pady=5)
        
        tk.Label(
            speed_frame,
            text="Typing Speed (WPM):",
            bg='#252526',
            fg='#cccccc',
            font=('Arial', 10)
        ).pack(side='left')
        
        self.speed_var = tk.IntVar(value=80)
        speed_spinbox = tk.Spinbox(
            speed_frame,
            from_=20,
            to=200,
            textvariable=self.speed_var,
            width=10,
            font=('Arial', 10),
            bg='#3c3c3c',
            fg='white',
            buttonbackground='#3c3c3c'
        )
        speed_spinbox.pack(side='left', padx=10)
        
        # Error rate
        error_frame = tk.Frame(settings_inner, bg='#252526')
        error_frame.pack(fill='x', pady=5)
        
        tk.Label(
            error_frame,
            text="Error Rate (%):",
            bg='#252526',
            fg='#cccccc',
            font=('Arial', 10)
        ).pack(side='left')
        
        self.error_var = tk.IntVar(value=2)
        error_spinbox = tk.Spinbox(
            error_frame,
            from_=0,
            to=10,
            textvariable=self.error_var,
            width=10,
            font=('Arial', 10),
            bg='#3c3c3c',
            fg='white',
            buttonbackground='#3c3c3c'
        )
        error_spinbox.pack(side='left', padx=10)
        
        # Checkboxes
        self.realistic_var = tk.BooleanVar(value=True)
        realistic_check = tk.Checkbutton(
            settings_inner,
            text="Realistic Pauses (thinking delays)",
            variable=self.realistic_var,
            bg='#252526',
            fg='#cccccc',
            selectcolor='#1e1e1e',
            font=('Arial', 10)
        )
        realistic_check.pack(anchor='w', pady=2)
        
        # Control section
        control_frame = tk.LabelFrame(
            main_frame,
            text="🎮 Controls",
            font=('Arial', 11, 'bold'),
            bg='#252526',
            fg='#ffffff',
            bd=2
        )
        control_frame.pack(fill='x', pady=(0, 10))
        
        control_inner = tk.Frame(control_frame, bg='#252526')
        control_inner.pack(fill='x', padx=10, pady=10)
        
        # Start button
        self.start_btn = tk.Button(
            control_inner,
            text="▶️ START TYPING (F9)",
            command=self.start_typing,
            bg='#16825d',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=30,
            pady=12,
            relief='flat',
            cursor='hand2'
        )
        self.start_btn.pack(side='left', padx=5)
        
        # Pause button
        self.pause_btn = tk.Button(
            control_inner,
            text="⏸️ PAUSE (F10)",
            command=self.toggle_pause,
            bg='#f0ad4e',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=30,
            pady=12,
            relief='flat',
            cursor='hand2',
            state='disabled'
        )
        self.pause_btn.pack(side='left', padx=5)
        
        # Stop button
        self.stop_btn = tk.Button(
            control_inner,
            text="⏹️ STOP (F11)",
            command=self.stop_typing,
            bg='#d9534f',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=30,
            pady=12,
            relief='flat',
            cursor='hand2',
            state='disabled'
        )
        self.stop_btn.pack(side='left', padx=5)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#007acc', height=30)
        status_frame.pack(fill='x', side='bottom')
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready to type! Load your code and press F9 to start (5 second delay)",
            bg='#007acc',
            fg='white',
            font=('Arial', 9),
            anchor='w',
            padx=10
        )
        self.status_label.pack(fill='x')
        
        # Instructions
        instructions = """
💡 Quick Start:
1. Load your code file or paste it above
2. Click on Arduino IDE (or any editor)
3. Press F9 to start typing (5 sec delay)
4. Press F10 to pause/resume
5. Press F11 to stop

⌨️ Hotkeys work globally (even when window is minimized!)
        """
        
        info_label = tk.Label(
            main_frame,
            text=instructions.strip(),
            bg='#1e1e1e',
            fg='#61dafb',
            font=('Arial', 9),
            justify='left',
            anchor='w'
        )
        info_label.pack(fill='x', pady=5)
    
    def setup_hotkeys(self):
        """Setup global hotkeys"""
        # Bind keys to root window
        self.root.bind('<F9>', lambda e: self.start_typing())
        self.root.bind('<F10>', lambda e: self.toggle_pause())
        self.root.bind('<F11>', lambda e: self.stop_typing())
    
    def load_file(self):
        """Load code from file"""
        filetypes = (
            ('Arduino Files', '*.ino'),
            ('C/C++ Files', '*.c *.cpp *.h'),
            ('Python Files', '*.py'),
            ('All Files', '*.*')
        )
        
        filename = filedialog.askopenfilename(
            title='Select Code File',
            filetypes=filetypes
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.code_text.delete('1.0', 'end')
                    self.code_text.insert('1.0', content)
                    self.update_status(f"✅ Loaded: {Path(filename).name}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file:\n{e}")
    
    def clear_code(self):
        """Clear code text area"""
        self.code_text.delete('1.0', 'end')
        self.update_status("Cleared code area")
    
    def update_status(self, message):
        """Update status bar"""
        self.status_label.config(text=message)
    
    def start_typing(self):
        """Start the typing simulation"""
        if self.is_typing:
            return
        
        code = self.code_text.get('1.0', 'end-1c').strip()
        if not code:
            messagebox.showwarning("No Code", "Please load or paste some code first!")
            return
        
        self.code_content = code
        self.is_typing = True
        self.pause_event.set()
        
        # Update UI
        self.start_btn.config(state='disabled')
        self.pause_btn.config(state='normal')
        self.stop_btn.config(state='normal')
        self.update_status("⏳ Starting in 5 seconds... Click on your editor window!")
        
        # Start typing in thread
        self.typing_thread = threading.Thread(target=self.type_code, daemon=True)
        self.typing_thread.start()
    
    def toggle_pause(self):
        """Pause or resume typing"""
        if not self.is_typing:
            return
        
        if self.pause_event.is_set():
            self.pause_event.clear()
            self.pause_btn.config(text="▶️ RESUME (F10)")
            self.update_status("⏸️ Paused - Press F10 to resume")
        else:
            self.pause_event.set()
            self.pause_btn.config(text="⏸️ PAUSE (F10)")
            self.update_status("▶️ Resumed typing...")
    
    def stop_typing(self):
        """Stop typing simulation"""
        self.is_typing = False
        self.pause_event.set()  # Unpause to allow thread to exit
        
        # Update UI
        self.start_btn.config(state='normal')
        self.pause_btn.config(state='disabled', text="⏸️ PAUSE (F10)")
        self.stop_btn.config(state='disabled')
        self.update_status("⏹️ Stopped")
    
    def type_code(self):
        """Main typing logic - runs in separate thread"""
        try:
            # Initial delay
            time.sleep(5)
            
            # Get settings
            wpm = self.speed_var.get()
            error_rate = self.error_var.get()
            realistic = self.realistic_var.get()
            
            # Calculate base delay between characters (WPM to chars per second)
            chars_per_minute = wpm * 5  # Average word is 5 chars
            base_delay = 60.0 / chars_per_minute
            
            lines = self.code_content.split('\n')
            total_lines = len(lines)
            
            for line_num, line in enumerate(lines, 1):
                if not self.is_typing:
                    break
                
                # Wait if paused
                self.pause_event.wait()
                
                # Update status
                self.update_status(f"⌨️ Typing... Line {line_num}/{total_lines}")
                
                # Type each character
                for char in line:
                    if not self.is_typing:
                        break
                    
                    self.pause_event.wait()
                    
                    # Random variation in typing speed
                    delay = base_delay * random.uniform(0.7, 1.3)
                    
                    # Simulate typing errors
                    if random.randint(1, 100) <= error_rate and char.isalpha():
                        # Type wrong character
                        wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
                        pyautogui.write(wrong_char, interval=0)
                        time.sleep(delay * 0.5)
                        # Backspace
                        pyautogui.press('backspace')
                        time.sleep(delay * 0.5)
                    
                    # Type the correct character
                    if char == '\t':
                        pyautogui.press('tab')
                    else:
                        pyautogui.write(char, interval=0)
                    
                    # Realistic pauses at punctuation
                    if realistic and char in '.;,':
                        time.sleep(delay * 2)
                    else:
                        time.sleep(delay)
                
                # Press Enter to go to next line
                if line_num < total_lines:
                    pyautogui.press('enter')
                    
                    # Pause after line
                    if realistic:
                        # Longer pause at end of code blocks
                        if line.strip().endswith(('{', '}', ';')):
                            time.sleep(random.uniform(0.5, 1.0))
                        else:
                            time.sleep(random.uniform(0.2, 0.5))
            
            # Finished
            self.update_status("✅ Finished typing!")
            self.stop_typing()
            
        except Exception as e:
            self.update_status(f"❌ Error: {e}")
            self.stop_typing()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = CodeTyper(root)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == '__main__':
    main()
