from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Informal Interview Guide for PWUDs", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

sections = [
    ("Start – Introduce Yourself & Get Consent (1–2 mins)",
     '"Hey, thanks for taking the time to chat with me. I’m just trying to learn more about what life’s like for folks who use drugs around here — what’s working, what’s not, what you wish people understood better. It’s super chill — no right or wrong answers. You can skip anything, and if you ever wanna stop, that’s totally fine too. Sound okay?"'),

    ("Warm-Up: Get to Know Them (2–3 mins)",
     '“To start off... can you tell me a little bit about yourself?”\n(Pause and let them lead. If they need help, guide with: where they\'re from, how long they’ve been in the area, etc.)\n\nFollow-up prompts:\n- “How’d you first get introduced to the stuff you use?”\n- “What’s your relationship with it been like over the years?”\n- “What’s a day in your life usually look like?”'),

    ("Talking About Services & Support (4–5 mins)",
     '“Have you ever tried using any kind of support — like a clinic, drop-in spot, outreach team, anything like that?”\n\nFollow-up prompts:\n- “How did that go for you?”\n- “Was there anything that made it hard to get help, or anything that made it easier?”\n- “Is there a place or person you really trust?”'),

    ("Harm Reduction & Safety (3–4 mins)",
     '“Some folks use programs like needle exchanges, safe use kits, or places to use more safely — is that something you\'ve come across?”\n\nFollow-up prompts:\n- “What kind of stuff helps you stay safe?”\n- “If you’ve used those kinds of services, how did you find out about them?”\n- “If not — what’s stopped you?”'),

    ("Wrap-Up: What They Wish Others Knew (3 mins)",
     '“If you had the chance to tell people — maybe service providers, maybe the general public — one thing about your life or your experience, what would it be?”\n\nFollow-up prompts:\n- “What do you wish existed that doesn\'t right now?”\n- “What would make things feel less stressful, or more fair?”\n- “Anything else you want to say or share before we wrap up?”'),

    ("End with Appreciation",
     '“Thanks for being real with me — I really appreciate you sharing your story. If you ever want to talk more or need anything, feel free to reach out. And again, you’re totally in control of what happens with what you said today.”')
]

for title, body in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output("Informal_Interview_Guide_for_PWUDs.pdf")
