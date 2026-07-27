# Design — Project Identity

> This document is project-long-lived. Tokens are not changed without
> the Architect's approval. Developers MUST use these tokens
> instead of improvising their own colors/spacings.

## Style Direction

Klares, helles Produktivitätstool mit ruhigem Blau als Akzent – fokussiert und aufgeräumt wie Linear, aber zugänglicher wie Trello.

## Colors

- `--color-bg`: **#FAFBFC**
- `--color-surface`: **#FFFFFF**
- `--color-fg`: **#1A1D23**
- `--color-accent`: **#3B6FF5**
- `--color-accent_hover`: **#2B5AD4**
- `--color-accent_active`: **#1E45A8**
- `--color-border`: **#E2E6EC**
- `--color-muted`: **#6B7280**
- `--color-danger`: **#DC3545**
- `--color-danger_hover`: **#C82333**
- `--color-success`: **#16A34A**
- `--color-column_todo`: **#F1F5F9**
- `--color-column_progress`: **#EFF6FF**
- `--color-column_done`: **#F0FDF4**

## Typography

- `font_family`: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif
- `heading_weight`: 600
- `body_weight`: 400
- `size_scale`: xs: 11px; sm: 13px; base: 15px; md: 17px; lg: 20px; xl: 26px; xxl: 32px

## Spacing Scale

- `--space-0`: 4px
- `--space-1`: 8px
- `--space-2`: 12px
- `--space-3`: 16px
- `--space-4`: 24px
- `--space-5`: 32px
- `--space-6`: 48px

## Border-Radii

- `--radius-sm`: 4px
- `--radius-md`: 8px
- `--radius-lg`: 12px
- `--radius-pill`: 999px

## Components

### Button / Primary

bg=accent(#3B6FF5), color=#FFFFFF, font-weight=600, font-size=14px, padding=10px 20px, radius=md(8px), border=none, cursor=pointer, min-height=44px, display=inline-flex, align-items=center, gap=8px. Hover: bg=accent_hover(#2B5AD4). Active: bg=accent_active(#1E45A8). Focus-visible: outline=2px solid #3B6FF5, outline-offset=2px. Disabled: opacity=0.5, cursor=not-allowed, pointer-events=none.

### Button / Secondary

bg=transparent, color=#1A1D23, font-weight=500, font-size=14px, padding=10px 20px, radius=md(8px), border=1px solid #E2E6EC, min-height=44px. Hover: bg=#F1F5F9, border=#CBD5E1. Active: bg=#E2E6EC. Disabled: opacity=0.5, cursor=not-allowed.

### Button / Danger

bg=#DC3545, color=#FFFFFF, font-weight=600, font-size=14px, padding=10px 20px, radius=md(8px), border=none, min-height=44px. Hover: bg=#C82333. Active: bg=#A71D2A. Disabled: opacity=0.5, cursor=not-allowed.

### Button / Ghost

bg=transparent, color=#6B7280, font-weight=500, font-size=13px, padding=6px 12px, radius=sm(4px), border=none, min-height=36px. Hover: bg=#F1F5F9, color=#1A1D23. Active: bg=#E2E6EC.

### Card (Kanban-Karte)

bg=#FFFFFF, border=1px solid #E2E6EC, radius=md(8px), padding=12px 14px, box-shadow=0 1px 2px rgba(0,0,0,0.04), cursor=grab, min-height=60px, width=100%, font-size=14px, color=#1A1D23. Hover: box-shadow=0 2px 8px rgba(0,0,0,0.08), border=#CBD5E1. Dragging: opacity=0.6, box-shadow=0 4px 16px rgba(0,0,0,0.12), cursor=grabbing. Card-title: font-weight=600, font-size=15px, margin-bottom=4px, line-height=1.4. Card-description: font-size=13px, color=#6B7280, line-height=1.5, margin-top=4px.

### Input (Textfeld)

bg=#FFFFFF, border=1px solid #E2E6EC, radius=md(8px), padding=10px 14px, font-size=15px, color=#1A1D23, min-height=44px, width=100%, font-family=inherit, outline=none. Placeholder: color=#9CA3AF. Hover: border=#CBD5E1. Focus: border=#3B6FF5, box-shadow=0 0 0 3px rgba(59,111,245,0.12). Error: border=#DC3545. Disabled: bg=#F9FAFB, color=#9CA3AF.

### Modal

Backdrop: bg=rgba(15,23,42,0.45), backdrop-filter=blur(2px), position=fixed, inset=0, z-index=100, display=flex, align-items=center, justify-content=center. Panel: bg=#FFFFFF, radius=lg(12px), padding=24px, max-width=480px, width=90vw, box-shadow=0 8px 32px rgba(0,0,0,0.12). Title: font-weight=600, font-size=18px, margin-bottom=16px. Body: font-size=15px, color=#1A1D23, margin-bottom=24px. Actions: display=flex, justify-content=flex-end, gap=12px.

### Column (Kanban-Spalte)

bg=#F1F5F9, radius=lg(12px), padding=14px, min-width=280px, flex=1, display=flex, flex-direction=column, gap=10px. Column-header: display=flex, align-items=center, justify-content=space-between, margin-bottom=6px. Column-title: font-weight=600, font-size=14px, color=#374151, text-transform=uppercase, letter-spacing=0.5px. Column-count: font-size=12px, color=#9CA3AF, bg=#FFFFFF, radius=pill(999px), padding=2px 10px, font-weight=500. Column-body: flex=1, display=flex, flex-direction=column, gap=10px, min-height=100px. Drop-indicator: border=2px dashed #3B6FF5, radius=md(8px), bg=rgba(59,111,245,0.04), min-height=60px. To-Do-Spalte: bg=#F1F5F9. In-Progress-Spalte: bg=#EFF6FF. Done-Spalte: bg=#F0FDF4.

### Header / App-Bar

bg=#FFFFFF, border-bottom=1px solid #E2E6EC, padding=0 24px, height=56px, display=flex, align-items=center, justify-content=space-between, position=sticky, top=0, z-index=50. Logo/Titel: font-weight=700, font-size=18px, color=#1A1D23. User-Section: display=flex, align-items=center, gap=12px. User-Email: font-size=13px, color=#6B7280. Logout-Button: vom Typ Ghost (siehe Button/Ghost).

### Auth-Form (Login/Register)

Card: bg=#FFFFFF, radius=lg(12px), padding=32px, max-width=400px, width=100%, box-shadow=0 2px 16px rgba(0,0,0,0.06), border=1px solid #E2E6EC. Title: font-weight=700, font-size=24px, color=#1A1D23, text-align=center, margin-bottom=24px. Input-Gruppe: display=flex, flex-direction=column, gap=16px, margin-bottom=24px. Label: font-weight=500, font-size=13px, color=#374151, margin-bottom=4px. Submit-Button: Breite=100%, Typ=Primary. Toggle-Link: font-size=13px, color=#3B6FF5, text-align=center, margin-top=16px, cursor=pointer, font-weight=500. Hover Toggle: text-decoration=underline. Error-Message: bg=#FEF2F2, color=#DC3545, font-size=13px, padding=10px 14px, radius=md(8px), margin-bottom=16px.

### Empty-State (leere Spalte / Board)

display=flex, flex-direction=column, align-items=center, justify-content=center, padding=32px 16px, color=#9CA3AF, font-size=13px, text-align=center. Icon/Illustration: optional, max-width=80px, opacity=0.3. Text: margin-top=8px, line-height=1.5.

### Toast / Notification

bg=#1A1D23, color=#FFFFFF, padding=12px 20px, radius=md(8px), font-size=14px, box-shadow=0 4px 16px rgba(0,0,0,0.15), position=fixed, bottom=24px, right=24px, z-index=200, animation=fadeIn 0.2s ease. Success-Variante: bg=#16A34A. Error-Variante: bg=#DC3545.

## Layout Principles

- Container max-width=1200px, horizontal zentriert (margin: 0 auto), padding-left/right=24px
- Board-Layout: display=flex, gap=20px, align-items=flex-start, overflow-x=auto, padding-top=24px, padding-bottom=48px, min-height=calc(100vh - 56px)
- Spalten gleich breit: flex=1, min-width=280px, max-width=380px (drei Spalten nebeneinander auf >=1024px)
- Responsive Breakpoints: <1024px horizontales Scrollen der Spalten erlauben; <640px Spalten untereinander (flex-direction=column), padding auf 12px reduzieren
- Seiten-Hintergrund: bg=#FAFBFC (Token colors.bg)
- Abstände zwischen Sektionen im Formular: 24px (Token spacing[4])
- Interaktive Elemente: min. Tap-Target 44px (Mobile), ausreichend Abstand zwischen klickbaren Elementen (min. 8px)
- Fokus-Indikatoren: bei allen interaktiven Elementen sichtbarer Focus-Ring (2px solid accent, 2px offset)
- Card-Grid in Spalten: vertikaler Abstand zwischen Karten 10px, Karten füllen die Spaltenbreite aus
