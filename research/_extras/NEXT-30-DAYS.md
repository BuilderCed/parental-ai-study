# Next 30 Days Action Plan

**Based on** : Complete user research (03-user-voice.md, 278 signals)  
**Goal** : Validate PMF, build MVP, or pivot  
**Timeline** : 4 weeks

---

## Week 1-2 : Validation Interviews

### Goal
Confirm pain ranking with target users. Test "Anticipation view" concept.

### Actions
- [ ] Find & schedule 20 interviews : **"Gestionnaire invisible" persona**
  - Profile : Mère 35-42, couple, 2-3 enfants (0-12), urbaine, CSP+, burnout risk
  - Channels : Instagram parenting, Doctissimo, local parenting groups
- [ ] Build interview guide (15 min interviews)
  - Q1-3 : Context (daily reality, pain stack)
  - Q4-6 : Core frustration (what's hardest?)
  - Q7-10 : Solution test (Anticipation view concept)
  - Q11-15 : Partner engagement (how to get husband on board?)
- [ ] Record findings in shared doc (pain ranking, quotes, feature reactions)

### Success Metrics
- 15-20 interviews completed
- Pain ranking validated or reordered
- Partner engagement insights collected
- 3-5 strong product insights extracted

**Owner** : CEO / PM  
**Time investment** : 40-50 hours

---

## Week 3-4 : MVP Concept & Prototype

### Goal
Validate Anticipation view concept. Design partner engagement mechanism. Plan MVP scope.

### Actions
- [ ] **Build Anticipation view prototype**
  - Week 1 : Lo-fi wireframe (pencil/Figma)
  - Week 2 : Interactive prototype (Figma/Lovable)
  - Show to 5 users : feedback on layout, usefulness, clarity
  
- [ ] **Design Partner dashboard**
  - Goal : Show visible asymmetry (non-blaming)
  - Example : "This week: You managed 28 tasks, Paul managed 3"
  - Test messaging : Validate "not accusatory" tone
  
- [ ] **Map school calendar API integration**
  - Research : Which schools expose calendars? (France: Pronote, etc.)
  - Plan : Auto-sync architecture (pull school events)
  - Estimate : effort to build integration
  
- [ ] **Plan IA suggestion engine**
  - Scope : Meal suggestions (based on preferences, budget, time)
  - Scope : Activity suggestions (based on kids' age, weather)
  - Research : Which LLM? (Claude, GPT, open-source)

### Success Metrics
- Prototype created + tested with 5 users
- Partner dashboard messaging validated
- API integration plan clear
- MVP scope defined (features vs later)

**Owner** : PM / Designer  
**Time investment** : 50-60 hours

---

## Week 4 : GO/NO-GO Decision

### Validation Checklist

**Pain validation** ✅
- [ ] "Je pense à tout" confirmed as top pain (#1)
- [ ] "Fallait demander" confirmed as couple friction (#2)
- [ ] 3+ quotes from interviews support messaging

**Solution validation** ✅
- [ ] Anticipation view = "useful" rating from 4/5 users
- [ ] Partner engagement concept = interest from 3/5 users
- [ ] Auto-sync school calendar = "must-have" for 4/5 users

**Market validation** ✅
- [ ] Segment exists (confirmed via interviews)
- [ ] Willingness to pay evident (from messaging reaction)
- [ ] Competitive gap confirmed (no one does this)

**Team alignment** ✅
- [ ] Founder = GO/NO-GO decision
- [ ] PM = feature prioritization clear
- [ ] Designer = aesthetic direction defined
- [ ] Go-to-market = channel strategy (Instagram + Doctissimo)

### Decision Framework

**GO** if:
- 3+ pain points confirmed across 15+ interviews
- Anticipation view NPS > 7/10
- Partner engagement interest from 3+ couples
- Team alignment on MVP scope

**NO-GO** if:
- Pain not validated (interviews show different #1 pain)
- Anticipation view NPS < 5/10
- Partner engagement not solvable (couples too entrenched)
- Team capacity insufficient

**PIVOT** if:
- Different segment more urgent (e.g., solo parents)
- Different feature more valuable (e.g., couple therapy integration)
- Different channel more efficient

---

## Week 4 Output : GO Decision

**Recommendation from research** : ✅ **GO**

**Why** :
1. Pain validated (278 signals, 30+ sources)
2. Solution clear (IA + anticipation + couple equity)
3. Whitespace real (Cozi/FamilyWall miss 80% of pain)
4. Market ready (parents already use IA secretly)
5. Timing right (Emma 2017 + UN Women 2025 normalized conversation)

**If research validates** : Proceed to MVP build.

**If research contradicts** : Update assumptions, pivot accordingly.

---

## Week 5+ : MVP Development (Conditional)

If GO decision confirmed:

### Phase 2A : Core Features (Weeks 5-8)
- [ ] Anticipation view (weekly calendar + what-to-think-about)
- [ ] Partner dashboard (visible asymmetry)
- [ ] Auto-sync school calendar
- [ ] IA suggestion engine (meals, activities)

### Phase 2B : Onboarding & Setup (Weeks 9-12)
- [ ] User onboarding flow
- [ ] Partner invitation flow
- [ ] Data import (Google Calendar, family info)
- [ ] Settings (preferences, notification rules)

### Phase 3 : Launch (Weeks 13-16)
- [ ] Target : Segment 1 (mères couple CSP+ urbain, France)
- [ ] Channels : Instagram parenting, Doctissimo, Reddit
- [ ] Messaging : "Voici votre charge mentale en chiffres"
- [ ] Metrics : NPS > 50, Partner adoption > 60%, D7 retention > 70%

---

## Resources Needed

### Team
- **CEO/Founder** : Strategy, interviews, go-to-market
- **Product Manager** : Feature design, MVP scope, validation
- **Designer/UX** : Prototype, user testing, interface design
- **Engineer** : Architecture planning, API integration

### Tools
- **Research** : Airtable/Notion (interview tracking)
- **Prototype** : Figma (design), Lovable (interactive)
- **Dev** : Next.js, Supabase, Claude API
- **Analytics** : PostHog (user behavior)

### Budget (estimate)
- User research (interviews, testing) : 2k-3k EUR
- Design/prototype : 1k-2k EUR
- MVP development : 5k-10k EUR (if building in-house)

---

## Key Risks to Monitor

### Risk 1 : Partner non-engagement (35% app failure reason)
**Mitigation** : Design partner onboarding flow to show value immediately. Test with couples during interviews (Week 1-2).

### Risk 2 : Data entry friction (45% app failure reason)
**Mitigation** : Auto-sync school calendar is non-negotiable. Plan API integration early (Week 3-4).

### Risk 3 : AI quality (suggestions not useful)
**Mitigation** : Test LLM quality early. May need fine-tuning or custom prompts.

### Risk 4 : Market reach (how to get users?)
**Mitigation** : Doctissimo partnerships, Instagram parenting influencers, Reddit communities. Plan Week 4.

---

## Success Metrics (Week 4 Decision)

| Metric | Target | Why |
|--------|--------|-----|
| **Interviews completed** | 15-20 | Validate pain ranking |
| **Pain ranking confirmed** | Top 3 match research | Validate hypothesis |
| **Anticipation view NPS** | > 7/10 | Confirm usefulness |
| **Partner engagement interest** | 3+ couples | Validate couple angle |
| **Team alignment** | 100% on scope | Clear MVP definition |

---

## Deliverables by Week

| Week | Deliverable | Format |
|------|------------|--------|
| **Week 1-2** | Interview findings | Airtable + summary doc + quotes |
| **Week 3-4** | Prototype + concept docs | Figma + Lovable link + specs |
| **Week 4** | GO/NO-GO decision | Decision doc + reasoning |
| **Week 5+** | MVP roadmap (if GO) | Jira/Notion + timeline |

---

## Communication Cadence

- **Daily** : Slack updates (team)
- **Weekly** : Team sync (30 min)
- **Week 2-end** : Interview synthesis (all hands)
- **Week 4-end** : GO/NO-GO decision meeting (leadership)

---

## Contingency

If things go slower than planned:
- Extend interviews into Week 3 (still okay)
- Compress prototype to lo-fi (skip interactive)
- Push decision to Week 5 (acceptable)

**But do not skip** :
- User interviews (non-negotiable)
- Partner engagement validation (non-negotiable)
- API integration planning (non-negotiable)

---

## Next Action

1. **CEO** : Read BLUF.md + EXECUTIVE-SUMMARY.md (5 min)
2. **PM** : Read 03-user-voice.md + insights-matrix.md (45 min)
3. **Designer** : Read EXECUTIVE-SUMMARY.md + 03-user-voice sections 1-4 (25 min)
4. **All** : Team sync this week → confirm plan + assign owners

**Week 1, Day 1** : Begin scheduling interviews.

---

**Status: READY TO VALIDATE**

