import customtkinter as ctk

# ── 1. Global appearance ──────────────────────────────────────────────
ctk.set_appearance_mode("dark")        # "dark" | "light" | "system"
ctk.set_default_color_theme("blue")    # accent colour: "blue" | "green" | "dark-blue"

# ── 2. Main window ───────────────────────────────────────────────────
app = ctk.CTk()
app.title("Hello World App")
app.geometry("400x300")
app.resizable(False, False)

# ── 3. Heading label ─────────────────────────────────────────────────
label = ctk.CTkLabel(
    app,
    text="Hello, World! 👋",
    font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"),
)
# pack() centres horizontally by default; pady adds breathing room above
label.pack(pady=(60, 10))

# ── 4. Sub-label ─────────────────────────────────────────────────────
subtitle = ctk.CTkLabel(
    app,
    text="Built with CustomTkinter",
    font=ctk.CTkFont(size=14),
    text_color="gray",
)
subtitle.pack(pady=(0, 30))

# ── 5. Rounded button ────────────────────────────────────────────────
def on_click():
    label.configure(text="Button clicked! 🎉")

btn = ctk.CTkButton(
    app,
    text="Click Me",
    width=160,
    height=40,
    corner_radius=20,         
    font=ctk.CTkFont(size=15, weight="bold"),
    command=on_click,
)
btn.pack(pady=10)

# ── 6. Start the event loop ──────────────────────────────────────────
app.mainloop()