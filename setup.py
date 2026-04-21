import os

base = os.path.dirname(os.path.abspath(__file__))

def write(path, content):
    full = os.path.join(base, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)
    print(f"✅ {path}")

write("src/pages/articles/does-copyright-happen-automatically-india.md", """---
layout: ../../layouts/ArticleLayout.astro
title: "Does Copyright Happen Automatically in India?"
description: "Yes — copyright arises automatically the moment you create something in India. But proving it is another matter entirely. Here's what creators need to know."
pubDate: "2026-04-21"
category: "Legal Education"
readTime: "5 min read"
canonicalUrl: "https://resources.nakid.in/articles/does-copyright-happen-automatically-india"
---

Copyright in India is automatic. The moment you write a story, compose a song, design a logo, or shoot a photograph — you own the copyright. No registration required. No forms to fill. No fees to pay.

This is established under the **Copyright Act, 1957**, which grants copyright protection automatically upon creation of an original work. India follows the same principle as most countries that are signatories to the Berne Convention.

## What Does "Automatic Copyright" Actually Mean?

It means that as soon as your original work exists in a fixed form — written down, recorded, saved as a file — it is protected by law. You have the exclusive right to:

- Reproduce your work
- Distribute copies
- Perform or display it publicly
- Create derivative works based on it
- License it to others

No one can legally copy, distribute, or use your work without your permission.

## The Problem: Proving You Created It First

Here's where things get complicated. Automatic copyright gives you rights — but it does not give you **proof**.

If someone steals your screenplay and claims they wrote it first, your copyright does not help you unless you can prove you created it before they did. In a legal dispute, the burden falls on you to establish:

1. That you are the original creator
2. When you created it
3. That your work predates the infringing work

Without documented proof, this is extremely difficult — even if you genuinely did create it first.

> This is the gap NAK-ID fills. When you register your work on NAK-ID, your file gets a permanent timestamp recorded on the Internet Computer blockchain. This gives you independently verifiable proof of creation — exactly what you would need in a dispute. [Register your work free on NAK-ID](https://nakid.in)

## What Counts as an Original Work?

Under Indian copyright law, the following types of works are protected:

- **Literary works** — novels, poems, scripts, articles, code
- **Musical works** — compositions, separate from sound recordings
- **Artistic works** — paintings, drawings, photographs, architecture
- **Cinematographic films** — including videos
- **Sound recordings** — the actual recording, separate from the composition
- **Dramatic works** — plays, screenplays, choreography

The work must be original — meaning it originated from you and involves some degree of creativity. It does not need to be novel or unique in the way a patent does.

## Does Copyright Registration in India Exist?

Yes. The Copyright Office of India allows voluntary registration under Section 45 of the Copyright Act. This creates a public record of your claim to ownership.

However, registration is not required for copyright to exist. It is optional.

That said, a registration certificate is useful evidence in court. The Copyright Office issues a certificate that serves as prima facie evidence of ownership.

Registration costs between Rs. 500 and Rs. 5,000 depending on the type of work, and the process can take several months.

## What About the Poor Man's Copyright?

You may have heard the advice to mail a copy of your work to yourself and leave the envelope sealed — the postmark supposedly proves the date of creation.

This is largely a myth. Indian courts do not reliably accept this as proof of copyright ownership. It has no legal standing under the Copyright Act and should not be relied upon.

## Practical Steps for Indian Creators

1. **Create your work** — copyright arises automatically
2. **Document the creation process** — save drafts, screenshots, emails
3. **Get a timestamped certificate** — services like NAK-ID give you permanent, verifiable proof of creation without the complexity of formal registration
4. **Consider formal copyright registration** for high-value works — especially films, software, and music

## The Bottom Line

Yes, copyright happens automatically in India. But automatic rights without documented proof are difficult to enforce. The smart move is to create a paper trail from the moment your work exists.

That is exactly what NAK-ID is built for.
""")

print("Chunk 6 done — all files created")