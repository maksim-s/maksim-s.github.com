---

layout: book
title: Superintelligence
category: book

book_notes: true
book_title: "Superintelligence: Paths, Dangers, Strategies"
book_author: Nick Bostrom
book_rating: 8
book_link: "http://www.amazon.com/Superintelligence-Dangers-Strategies-Nick-Bostrom/dp/0199678111/"
book_read_year: 2015
book_image: "superintelligence.jpg"

---

Below are the notes/bullet points I wrote down while reading [Nick Bostrom's "Superintelligence: Paths, Dangers, Strategies"](http://www.amazon.com/Superintelligence-Dangers-Strategies-Nick-Bostrom/dp/0199678111/). They were mostly notes for my future self, but I decided to start publishing all of my reading notes on this blog. Hopefully, someone else finds them useful too, but I will not be sad if I'm the only person who will ever read them :)

## Paths To Superintelligence
There are 5 different, but not mutually-exclusive, ways we can get to a greater-than-human intelligence:

- __Artificial intelligence__: programming a general AI that can improve recursively
- __Whole brain emulation__: scanning and closely modeling the computational structure of a biological brain and then improving it
- __Biological cognition__: enhancing the functioning of biological brains (nootropics, eugenics)
- __Brain-computer interfaces__: augmenting biological brains with computer implants
- __Networks and organizations__: combining individual weaker intelligences into networks to achieve “collective superintelligence”

## Forms Of Superintelligence

- __Speed superintelligence__: can do everything a human intellect can, but much faster.
- __Collective superintelligence__: composed of a large number of weaker intellects such that it outperforms any current cognitive system across many general domains
- __Quality superintelligence__: at least as fast as a human brain, but qualitatively smarter

## Digital Intelligence Advantages Over Biological

- speed of computational elements
- internal communication speed
- storage capacity and number of computational elements not limited by any factors
- reliability and lifespan
- editability of the software
- duplicability
- goal coordination by duplicating
- memory sharing
- new modules, modalities, and algorithms

## The Superintelligent Will

- __Orthogonality thesis__: intelligence and final goals are independent variables: any level of intelligence can be combined with any final goal
- __Instrumental convergence thesis__: superintelligent agents for a wide range of final goals will pursue similar intermediary goals to help them advance towards the final goal. For example:
    - self preservation
    - goal-content integrity
    - cognitive enhancement
    - technological perfection
    - resource acquisition

## Failure Modes

- __Perverse instantiation__: mismatch between the intention of the goal and the way the AI decides to satisfy it. For example: goal: make humans happy, perverse instantiation: implant electrodes into the pleasure center of human brains
- __Infrastructure profusion__: an agent transforms large part of the reachable universe into a resource to help it achieve its final goal. For example: goal: maximize the manufacture of paperclips, result: convert the Earth and then large chunks of the observable universe into paperclips
- __Mind crime__: moral and ethical problems that arise when the AI creates and kills of simulated minds.

## The Control Problem

- __Capability control__: control what superintelligence can do
    - _boxing method_: allow the system to interact with the outside world only via specific restricted channels
    - _incentive method_: align incentives of an agent with the principal’s interest (e.g. social integration with other equally powerful entities, cryptographic reward tokens)
    - _stunting_: limit system’s intellectual faculties or access to information (e.g. running on slow hardware, restricting incoming information,)
    - _tripwires_: perform testing and monitoring of the system, without its knowledge, and shut it down if any dangerous/suspicious activity is detected
- __Motivation selection__: control what superintelligence whats to do
    - _direct specification_: directly specified motivation system (this is extremely hard to do)
    - _domesticity_: motivate the system to act on a small scale, within a narrow context, and through a limited set of actions (e.g. oracle - only answering questions)
    - _indirect normativity_: indirect specification of the rules and values. For example: “achieve that which we would have wished the AI to achieve if we had thought about the matter long and hard”
    - _augmentation_: start with a good system and enhance it. This would work for brain emulation, biological enhancement, brain-computer interface, and network and organizations types of superintelligence

## Superintelligence Castes

- __Oracle__: a question-answering system
    - boxing methods and domesticity fully applicable
    - no need to understand human intentions and interests
    - results can be verified by asking questions such that the answers are hard to find, but easy to verify
    - weak verification can be done by using multiple oracles to verify each other
- __Genie__: a command-executing system
    - boxing methods and domesticity partially applicable
    - greater need to understand human intentions compared to oracles
    - can execute the command in stages for verification
    - can offer a preview of results before executing the commands
- __Sovereign__: a system design for open-ended autonomous operations
    - most of capability control methods are inapplicable
    - great need to understand human intentions
    - have to get it right the first time to avoid a catastrophic outcome
- __Tool-AI__: a system designed not to exhibit goal-directed behavior
    - powerful search may result in solutions that meet the criteria in an unintended and dangerous ways

## Value Loading Problem
The problem of loading values into an artificial agent to make it pursue the value as its final goal.

- __Evolutionary selection__
    - problems with mind crime while searching
    - search may find a design satisfying the criteria in an unintended way
    - if designs are evaluated by running them, then there’s a danger of running a design that does not meet the criteria
- __Reinforcement learning__
    - a system that tries to maximize some reward signal
    - the goal remains to maximize future reward, not to find and load correct values as the final goal
- __Value accretion__
    - humans acquire a lot of the values from the reactions to experience
    - very hard to make it work for seed AI vs. brain emulation
- __Motivational scaffolding__
    - start with simpler goals that can be fully specified directly and once the AI reaches that level, replace with more sophisticated goals
    - since these are final goals, the AI might resist to their replacement
    - AI might become too powerful while it’s still running with an interim goal
    - not clear how the final goal will be loaded, so just postponing the problem
- __Value learning__
    - using AI intelligence to learn the values we want it to pursue
    - AI acts according to its best estimates of the implicitly defined values
    - continually refines the estimates as it learns more
    - in contrast to scaffolding, the final value doesn’t change
- __Emulation modulation__
    - can only be used for brain emulation
    - modulate the motivation system of the emulated brain by administering digital equivalents of psychoactive drugs
    - not clear how precise such modulation can get
- __Institution design__
    - a system where artificial agents with the proper values loaded in them monitor the development of slightly smarter systems
    - the final system is a pyramid with humans (weakest intelligence, proper values, the most control) at the top and the smartest agents at the bottom (strongest intelligence, values still being monitored by higher levels of the pyramid, no control)

## Value Choosing Problem
Suppose we can load the values into the system, now we need to decide what values to load.

- __Indirect normativity__: we don’t know enough in our current state to define concrete standards, so we specify something abstract in hope that superintelligence could find a concrete standard in the future.
- __Coherent extrapolated volition - CEV__: “Our coherent extrapolated volition is our wish if we knew more, thought faster, were more the people we wished we were, had grown up farther together; where the extrapolation converges rather than diverges, where our wishes cohere rather than interfere; extrapolated as we wish that extrapolated, interpreted as we wish that interpreted.” - Eliezer Yudkowski
- __Moral rightness - MR__
    - instead of implementing CEV, the AI will do what’s morally right
    - hoping that superintelligence can understand morality better than we do
    - might not be what we actually want, even though it’s morally right
- __Moral permissibility - MP__
    - allow the AI to pursue CEV, as long as it doesn’t do anything morally impermissible
    - enactment MR or MP introduces a risk that humanity is sacrificed for a “greater good”
- __Components__:
    - _Goal content_: what objective should the AI pursue
    - _Decision theory_: what decision theory should the AI use when making decisions
    - _Epistemology_: what should the prior probability function be and what other assumptions about the world should the AI make
    - _Ratification_: shoud AI’s actions be subject to review by humans? what should the process be like?
