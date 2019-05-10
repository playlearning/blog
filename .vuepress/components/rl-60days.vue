<template>
    <div id='rl60days'>
        <h3 class="header-title"><a class="title" href="https://github.com/andri27-ts/60_Days_RL_Challenge">60 Days RL Challenge</a></h3>
        <p>Learn Deep Reinforcement Learning in Depth in 60 days</p>
        <ul class='two-col'>
            <li><strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge#week-1---introduction">Week 1 - Introduction</a></strong></li>
            <ul>
                <li><strong><a href="https://www.youtube.com/watch?v=JgvyzIkgxF0" rel="nofollow">An introduction to Reinforcement Learning</a> by Arxiv Insights</strong></li>
                <li><strong><a href="https://www.youtube.com/watch?v=Q4kF8sfggoI&amp;index=1&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3" rel="nofollow">Introduction and course overview</a> - CS294 by Levine</strong></li>
                <li><strong><a href="http://karpathy.github.io/2016/05/31/rl/" rel="nofollow">Deep Reinforcement Learning: Pong from Pixels</a> by Karpathy</strong></li>
            </ul>
            <li>
                <strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge#week-2---rl-basics-mdp-dynamic-programming-and-model-free-control">Week 2 - RL Basics</a></strong>
                <ul>
<li><strong><a href="https://www.youtube.com/watch?v=lfHX2hHRMVQ&amp;list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-&amp;index=2" rel="nofollow">Markov Decision Process</a></strong> RL by David Silver
<ul>
<li>Markov Processes</li>
<li>Markov Decision Processes</li>
</ul>
</li>
</ul>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=Nd1-UUMVfz4&amp;list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-&amp;index=3" rel="nofollow">Planning by Dynamic Programming</a></strong>  RL by David Silver
<ul>
<li>Policy iteration</li>
<li>Value iteration</li>
</ul>
</li>
</ul>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=PnHCvfgC_ZA&amp;index=4&amp;list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-" rel="nofollow">Model-Free Prediction</a></strong>  RL by David Silver
<ul>
<li>Monte Carlo Learning</li>
<li>Temporal Difference Learning</li>
<li>TD(λ)</li>
</ul>
</li>
</ul>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=0g4j2k_Ggc4&amp;list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-&amp;index=5" rel="nofollow">Model-Free Control</a></strong>  RL by David Silver
<ul>
<li>Ɛ-greedy policy iteration</li>
<li>GLIE Monte Carlo Search</li>
<li>SARSA</li>
<li>Importance Sampling</li>
</ul>
</li>
</ul>
            </li>

            <li>
                <strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge#week-3---value-function-approximation-and-dqn">Week 3 - Value Function Approximation and DQN</a></strong>
                <ul>
<li><strong><a href="https://www.youtube.com/watch?v=UoPei5o4fps&amp;list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ&amp;index=6" rel="nofollow">Value functions approximation</a> - RL by David Silver</strong>
<ul>
<li>Differentiable function approximators</li>
<li>Incremental methods</li>
<li>Batch methods (DQN)</li>
</ul>
</li>
</ul>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=nZXC5OdDfs4&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;index=7" rel="nofollow">Advanced Q-learning algorithms</a> - DRL UC Berkley by Sergey Levine</strong>
<ul>
<li>Replay Buffer</li>
<li>Double Q-learning</li>
<li>Continous actions (NAF,DDPG)</li>
<li>Pratical tips</li>
</ul>
</li>
</ul>
            </li>
            <li>
                <strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge#week-4---policy-gradient-methods-and-a2c">Week 4 - Policy gradient methods and A2C</a></strong>
    <ul>
<li><strong><a href="https://www.youtube.com/watch?v=KHZVXao4qXs&amp;list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ&amp;index=7" rel="nofollow">Policy gradient Methods</a> - RL by David Silver</strong>
<ul>
<li>Finite Difference Policy Gradient</li>
<li>Monte-Carlo Policy Gradient</li>
<li>Actor-Critic Policy Gradient</li>
</ul>
</li>
</ul>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=XGmd3wcyDg8&amp;t=0s&amp;list=PLkFD6_40KJIxJMR-j5A1mkxK26gh_qg37&amp;index=3" rel="nofollow">Policy gradient intro</a> - CS294-112 by Sergey Levine (RECAP, optional)</strong>
<ul>
<li>Policy Gradient (REINFORCE and Vanilla PG)</li>
<li>Variance reduction</li>
</ul>
</li>
</ul>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=Tol_jw5hWnI&amp;list=PLkFD6_40KJIxJMR-j5A1mkxK26gh_qg37&amp;index=4" rel="nofollow">Actor-Critic</a> - CS294-112 by Sergey Levine (More in depth)</strong>
<ul>
<li>Actor-Critic</li>
<li>Discout factor</li>
<li>Actor-Critic algorithm design (batch mode or online)</li>
<li>state-dependent baseline</li>
</ul>
</li>
</ul>
            </li>
            <li>
                <strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge#week-5---advanced-policy-gradients---trpo--ppo">Week 5 - Advanced Policy Gradients - TRPO &amp; PPO</a></strong>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=ycCtmp4hcUs&amp;t=0s&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;index=15" rel="nofollow">Advanced policy gradients</a> - CS294-112 by Sergey Levine</strong>
<ul>
<li>Problems with "Vanilla" Policy Gradient Methods</li>
<li>Policy Performance Bounds</li>
<li>Monotonic Improvement Theory</li>
<li>Algorithms: NPO, TRPO, PPO</li>
</ul>
</li>
</ul>
<ul>
<li><strong><a href="https://www.youtube.com/watch?v=xvRrgxcpaHY" rel="nofollow">Natural Policy Gradients, TRPO, PPO</a> - John Schulman, Berkey DRL Bootcamp - (RECAP, optional)</strong>
<ul>
<li>Limitations of "Vanilla" Policy Gradient Methods</li>
<li>Natural Policy Gradient</li>
<li>Trust Region Policy Optimization, TRPO</li>
<li>Proximal Policy Optimization, PPO</li>
</ul>
</li>
</ul>
            </li>
            <li>
                <strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge#week-6---evolution-strategies-and-genetic-algorithms">Week 6 - Evolution Strategies and Genetic Algorithms</a></strong>
<ul>
<li><strong>Evolution Strategies</strong>
<ul>
<li><a href="http://blog.otoro.net/2017/10/29/visual-evolution-strategies/" rel="nofollow">Intro to ES: A Visual Guide to Evolution Strategies</a></li>
<li><a href="http://blog.otoro.net/2017/11/12/evolving-stable-strategies/" rel="nofollow">ES for RL: Evolving Stable Strategies</a></li>
<li><a href="https://www.youtube.com/watch?v=SQtOI9jsrJ0&amp;feature=youtu.be" rel="nofollow">Derivative-free Methods - Lecture</a></li>
<li><a href="https://blog.openai.com/evolution-strategies/" rel="nofollow">Evolution Strategies (paper discussion)</a></li>
</ul>
</li>
<li><strong>Genetic Algorithms</strong>
<ul>
<li><a href="https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3" rel="nofollow">Introduction to Genetic Algorithms — Including Example Code</a></li>
</ul>
</li>
</ul>
            </li>
            <li>
                <strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge#week-7---model-based-reinforcement-learning">Week 7 - Model-Based reinforcement learning</a></strong>
<ul>
<li><strong>Model-Based RL by Davide Silver (Deepmind) (concise version)</strong>
<ul>
<li><a href="https://www.youtube.com/watch?v=ItMutbeOHtc&amp;index=8&amp;list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ" rel="nofollow">Integrating Learning and Planning</a>
<ul>
<li>Model-Based RL Overview</li>
<li>Integrated architectures</li>
<li>Simulation-Based search</li>
</ul>
</li>
</ul>
</li>
<li><strong>Model-Based RL by Sergey Levine (Berkley) (in depth version)</strong>
<ul>
<li><a href="https://www.youtube.com/watch?v=yap_g0d7iBQ&amp;index=9&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3" rel="nofollow">Learning dynamical systems from data</a>
<ul>
<li>Overview of model-based RL</li>
<li>Global and local models</li>
<li>Learning with local models and trust regions</li>
</ul>
</li>
<li><a href="https://www.youtube.com/watch?v=AwdauFLan7M&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;index=10" rel="nofollow">Learning policies by imitating optimal controllers</a>
<ul>
<li>Backpropagation into a policy with learned models</li>
<li>Guided policy search algorithm</li>
<li>Imitating optimal control with DAgger</li>
</ul>
</li>
<li><a href="https://www.youtube.com/watch?v=vRkIwM4GktE&amp;index=11&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3" rel="nofollow">Advanced model learning and images</a>
<ul>
<li>Models in latent space</li>
<li>Models directly in image space</li>
<li>Inverse models</li>
</ul>
</li>
</ul>
</li>
</ul>
            </li>
            <li>
                <strong><a href="https://github.com/andri27-ts/60_Days_RL_Challenge/blob/master/README.md#week-8---advanced-concepts-and-project-of-your-choice">Week 8 - Advanced Concepts and Project Of Your Choice</a></strong>
<ul>
<li>Sergey Levine (Berkley)
<ul>
<li><a href="https://www.youtube.com/watch?v=iOYiPhu5GEk&amp;index=13&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;t=0s" rel="nofollow">Connection between inference and control</a></li>
<li><a href="https://www.youtube.com/watch?v=-3BcZwgmZLk&amp;index=14&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;t=0s" rel="nofollow">Inverse reinforcement learning</a></li>
<li><a href="https://www.youtube.com/watch?v=npi6B4VQ-7s&amp;index=16&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;t=0s" rel="nofollow">Exploration (part 1)</a></li>
<li><a href="https://www.youtube.com/watch?v=0WbVUvKJpg4&amp;index=17&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;t=0s" rel="nofollow">Exploration (part 2) and transfer learning</a></li>
<li><a href="https://www.youtube.com/watch?v=UqSx23W9RYE&amp;index=18&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;t=0s" rel="nofollow">Multi-task learning and transfer</a></li>
<li><a href="https://www.youtube.com/watch?v=Xe9bktyYB34&amp;index=18&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3" rel="nofollow">Meta-learning and parallelism</a></li>
<li><a href="https://www.youtube.com/watch?v=mc-DtbhhiKA&amp;index=20&amp;list=PLkFD6_40KJIznC9CDbVTjAF2oyt8_VAe3&amp;t=0s" rel="nofollow">Advanced imitation learning and open problems</a></li>
</ul>
</li>
<li>David Silver (Deepmind)
<ul>
<li><a href="https://www.youtube.com/watch?v=N1LKLc6ufGY&amp;feature=youtu.be" rel="nofollow">Classic Games</a></li>
</ul>
</li>
</ul>
            </li>
        </ul>
    </div>
</template>

<style scoped>
#rl60days {
    background-color: #f8f8f8;
    padding: 1em 2em;
    margin-top: 1em;
    border-radius: 2px;
    font-size: 0.9em;
}
#rl60days>ul>li>strong>a {
    border-bottom: 1px dotted;
}
.title {
    color: #000;
    font-weight: bold;
}
.two-col {
    -webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;
}
p {
    margin: 0 0 10px;
    font-family: 'Raleway';
}
.header-title {
    padding: 0;
    margin: 0.25em 0 0 0;
}
</style>
