from manim import *
from manim_slides import Slide

config.background_color = WHITE
VMobject.set_default(color=BLACK)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING DefineI

class DefineI(Slide):
    def construct(self):
        definition = VGroup(
            Tex(r"Let $\mathbb{I}$ denote the set of all closed intervals in [0, 1]"),
            Tex(r"Given $a \in \mathbb{I}$, let $\overline{a}, \underline{a} \in [0,1]$ such that $a = [\underline{a}, \overline{a}]$"),
        ).arrange(DOWN, buff=0.4)
        self.play(Write(definition))
        self.next_slide()
        self.play(definition.animate.to_edge(UP))

        we_define_text = Tex(r"We define ")
        order_text_rest = Tex(r"$\sqsubseteq$ in $\mathbb{I}$ by: ")
        order_math = MathTex(r"a \sqsubseteq b \iff \underline{b} \leq \underline{a} \text{ and } \overline{a} \leq \overline{b}")
        order_full = VGroup(we_define_text, order_text_rest, order_math).arrange(RIGHT, buff=0.2)

        self.play(Write(order_full))
        self.next_slide()
        self.play(order_full.animate.next_to(definition, DOWN, buff=0.4))

        ax = NumberLine(
            x_range=[0, 1, 0.1],
            length=8,
            include_numbers = True,
            include_tip = False,
            exclude_origin_tick = False,
        ).next_to(order_full, DOWN, buff=3)
        self.play(Create(ax))

        interval_a = [0.3, 0.7]
        interval_b = [0.2, 0.8]

        rect_a = Rectangle(
            width = (interval_a[1] - interval_a[0]) * ax.unit_size,
            height = 0.5,
            color = BLUE,
            fill_opacity = 0.4,
        ).move_to(ax.number_to_point((interval_a[0] + interval_a[1]) / 2) + (0,0.6,0))
        label_a = MathTex("a", color=BLUE).next_to(rect_a, RIGHT)
        group_a = VGroup(rect_a, label_a)

        rect_b = Rectangle(
            width = (interval_b[1] - interval_b[0]) * ax.unit_size,
            height = 0.5,
            color = RED,
            fill_opacity = 0.4
        ).move_to(ax.number_to_point((interval_b[0] + interval_b[1]) / 2) + (0,1.2,0))
        label_b = MathTex("b", color=RED).next_to(rect_b, RIGHT)
        group_b = VGroup(rect_b, label_b)

        self.play(FadeIn(group_a), FadeIn(group_b))
        self.next_slide()

        remaining_order_group = VGroup(order_text_rest, order_math)
        self.play(FadeOut(definition), FadeOut(we_define_text), remaining_order_group.animate.arrange(RIGHT, buff=0.2).to_edge(UP))
        self.next_slide()

        new_interval_a = [0.3, 0.9]
        new_rect_a = Rectangle(
            width = (new_interval_a[1] - new_interval_a[0]) * ax.unit_size,
            height = 0.5,
            color = BLUE,
            fill_opacity = 0.4
        ).move_to(ax.number_to_point((new_interval_a[0] + new_interval_a[1]) / 2) + (0,0.6,0))
        new_label_a = MathTex("a", color=BLUE).next_to(new_rect_a, RIGHT)

        self.play(
            Transform(rect_a, new_rect_a),
            Transform(label_a, new_label_a)
        )
        self.next_slide()

        question_text = MathTex(r"a \sqsubseteq b?").next_to(remaining_order_group, DOWN, buff=2)
        self.play(Write(question_text))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING DefineEmbeddingFunction

class DefineEmbeddingFunction(Slide):
    def construct(self):
        definition_text = VGroup(
            Tex(r"$E : \mathbb{I} \times \mathbb{I} \to [0, 1]$ is an embedding on $\mathbb{I}$ when, $\forall a, b, c \in \mathbb{I}$:"),
        ).to_edge(UP)
        self.play(Write(definition_text))
        self.next_slide()

        properties = VGroup(
            Tex(r"A1: $E(a,b) = 1 \iff a \sqsubseteq b$"),
            Tex(r"A2: $a \neq \emptyset$ and $a \cap b = \emptyset \implies E(a,b) = 0$"),
            Tex(r"A3: $b \sqsubseteq c \implies E(a,b) \leq E(a,c)$"),
            Tex(r"A4: $a \sqsubseteq b \sqsubseteq c \implies E(c,a) \leq E(b,a)$")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT)


        for prop in properties:
            self.play(Write(prop))
            self.next_slide()

        explanation_text = Tex(
            r"A fuzzy relation that extends the binary relation of embedding.",
        ).to_edge(DOWN)

        self.play(Write(explanation_text))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING Proposition

class Proposition(Slide):
    def construct(self):
        proposition = VGroup(
            Tex(r"Let $I$ be a residual implication and $E : \mathbb{I} \times \mathbb{I} \to [0, 1]$"),
            MathTex(
                r"E(a, b) =",
                r"\begin{cases} 0  \text{   if } a \cap b = \emptyset \\ I(\underline{b}, \underline{a}) \wedge I(\overline{a}, \overline{b}) \end{cases}",
                r"\implies E \text{ is an embedding}"
            )
        ).arrange(DOWN, buff=1.5)

        self.play(Write(proposition))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofA1

class ProofA1(Slide):
    def construct(self):
        a1_goal = Tex(r"Proof of A1: $E(a, b) = 1 \iff a \sqsubseteq b$").to_edge(UP)
        self.play(Write(a1_goal))

        a1_proof = VGroup(
            MathTex(r"E(a, b) = 1"),
            MathTex(r"\iff I(\underline{b}, \underline{a}) \wedge I(\overline{a}, \overline{b}) = 1"),
            MathTex(r"\iff I(\underline{b}, \underline{a}) = 1 \text{ and } I(\overline{a}, \overline{b}) = 1"),
            MathTex(r"\iff \underline{b} \leq \underline{a} \text{ and } \overline{a} \leq \overline{b}"),
            MathTex(r"\iff a \sqsubseteq b"),
        ).arrange(DOWN, aligned_edge=LEFT)

        for step in a1_proof:
            self.play(Write(step))
            self.next_slide()

        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofA2

class ProofA2(Slide):
    def construct(self):
        a2_goal = Tex(r"Proof of A2: $a \cap b = \emptyset \implies E(a, b) = 0$").to_edge(UP)
        self.play(Write(a2_goal))

        a2_proof = Tex(r"This follows trivially from the definition of $E$.")
        self.play(Write(a2_proof))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofA3

class ProofA3(Slide):
    def construct(self):
        a3_goal = Tex(r"Proof of A3: $b \sqsubseteq c \implies E(a, b) \leq E(a, c)$").to_edge(UP)
        self.play(Write(a3_goal))

        a3_proof = VGroup(
            Tex(r"$b \sqsubseteq c \implies \underline{c} \le \underline{b} \text{ and } \overline{b} \le \overline{c}$."),
            Tex(r"Since $I$ is decreasing in the first variable: $I(\underline{b}, \underline{a}) \le I(\underline{c}, \underline{a})$."),
            Tex(r"Since $I$ is increasing in the second variable: $I(\overline{a}, \overline{b}) \le I(\overline{a}, \overline{c})$."),
            Tex(r"Therefore:"),
            MathTex(r"I(\underline{b}, \underline{a}) \wedge I(\overline{a}, \overline{b}) \le I(\underline{c}, \underline{a}) \wedge I(\overline{a}, \overline{c})"),
            MathTex(r"\implies E(a, b) \leq E(a, c)"),
        ).arrange(DOWN, aligned_edge=LEFT)

        for step in a3_proof:
            self.play(Write(step))
            self.next_slide()

        self.play(FadeOut(*self.mobjects))

# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofA4

class ProofA4(Slide):
    def construct(self):
        a4_goal = Tex(r"Proof of A4: $a \sqsubseteq b \sqsubseteq c \implies E(c, a) \leq E(b, a)$").to_edge(UP)
        self.play(Write(a4_goal))

        a4_proof = VGroup(
            Tex(r" $a \sqsubseteq b \sqsubseteq c \implies \underline{c} \le \underline{b} \le \underline{a} \text{ and } \overline{a} \le \overline{b} \le \overline{c}$."),
            Tex(r"Since $I$ is increasing in the second variable: $I(\underline{a}, \underline{c}) \le I(\underline{a}, \underline{b})$."),
            Tex(r"Since $I$ is decreasing in the first variable: $I(\overline{c}, \overline{a}) \le I(\overline{b}, \overline{a})$."),
            Tex(r"$E(c, a) = I(\underline{a}, \underline{c}) \wedge I(\overline{c}, \overline{a})$ and $E(b, a) = I(\underline{a}, \underline{b}) \wedge I(\overline{b}, \overline{a})$"),
            MathTex(r"\implies E(c, a) \leq E(b, a)"),
        ).arrange(DOWN, aligned_edge=LEFT)

        for step in a4_proof:
            self.play(Write(step))
            self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING SimilarityMeasureDef

class SimilarityMeasureDef(Slide):
    def construct(self):
        definition_text = Tex(
            r"$S : \mathbb{I} \times \mathbb{I} \to [0, 1]$ is a similarity measure for intervals if:"
        ).to_edge(UP)

        self.play(Write(definition_text))
        self.next_slide()

        properties = VGroup(
            Tex(r"For all $a, b, c \in \mathbb{I}$"),
            Tex(r"S1: $S(a, b) = S(b, a)$"),
            Tex(r"S2: $S(a, b) = 1 \iff a = b$"),
            Tex(r"S3: If $a \sqsubseteq b \sqsubseteq c$ then $S(a, c) \le S(a, b)$ and $S(a, c) \le S(b, c)$")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        for prop in properties:
            self.play(Write(prop))
            self.next_slide()

        extension_text = Tex(r"A fuzzy relation that extends the binary relation of equality.").next_to(properties, DOWN, buff=1)
        self.play(Write(extension_text))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING Proposition3

class Proposition3(Slide):
    def construct(self):

        t1 = Tex(r"Let $E : \mathbb{I} \times \mathbb{I} \to [0, 1]$ be an embedding").to_edge(UP)
        t2 = Tex(r"$S(a, b) = \frac{E(a, b) + E(b, a)}{2}$ is a similarity measure for intervals")

        self.play(Write(t1))
        self.play(Write(t2))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofS1

class ProofS1(Slide):
    def construct(self):
        s1_goal = Tex(r"Proof of S1: $S(a, b) = S(b, a)$").to_edge(UP)
        s1_proof = Tex(r"Symmetry follows from the definition of $S$.")

        self.play(Write(s1_goal))
        self.play(Write(s1_proof))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofS2

class ProofS2(Slide):
    def construct(self):
        s2_goal = Tex(r"Proof of S2: $S(a, b) = 1 \iff a = b$").to_edge(UP)
        s2_proof = VGroup(
            MathTex(r"S(a, b) = \frac{E(a, b) + E(b, a)}{2} = 1"),
            MathTex(r"\iff E(a, b) = 1 \text{ and } E(b, a) = 1"),
            MathTex(r"\iff a \sqsubseteq b \text{ and } b \sqsubseteq a"),
            MathTex(r"\iff a = b")
        ).arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(s2_goal))
        for step in s2_proof:
            self.play(Write(step))
            self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofS3

class ProofS3(Slide):
    def construct(self):
        s3_goal = Tex(r"Proof of Axiom 4: $a \sqsubseteq b \sqsubseteq c \implies \begin{gathered} S(a, c) \le S(a, b) \text{ and} \\ S(a, c) \le S(b, c) \end{gathered}$").to_edge(UP)
        self.play(Write(s3_goal))
        self.next_slide()

        proof_part1 = VGroup(
             MathTex(r"S(a, c) = \frac{E(a,c) + E(c, a)}{2} = \frac{1 + E(c, a)}{2}"),
             MathTex(r"\le \frac{1 + E(b, a)}{2} \quad (\text{since } E(c,a) \le E(b,a))"),
             MathTex(r"= \frac{E(a, b) + E(b, a)}{2} \quad (\text{since } a \sqsubseteq b \implies E(a,b)=1)"),
             MathTex(r"= S(a, b)")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(s3_goal, DOWN, buff=0.5)

        for step in proof_part1:
            self.play(Write(step))
            self.next_slide()

        self.play(FadeOut(proof_part1))

        proof_part2 = VGroup(
             MathTex(r"S(a, c) = \frac{E(a, c) + E(c, a)}{2} = \frac{1 + E(c, a)}{2}"),
             MathTex(r"\le \frac{1 + E(c, b)}{2} \quad (\text{since } E(c,a) \le E(c,b))"),
             MathTex(r"= \frac{E(b, c) + E(c, b)}{2} \quad (\text{since } b \sqsubseteq c \implies E(b,c)=1)"),
             MathTex(r"= S(b, c)")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(s3_goal, DOWN, buff=0.5)

        for step in proof_part2:
            self.play(Write(step))
            self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING DefineIVFSEmbedding

class DefineIVFSEmbedding(Slide):
    def construct(self):
        definition_ivfs = VGroup(
            Tex(r"An interval-valued fuzzy set (IVFS) on a universe $X$ is a "),
            Tex(r"mapping in $\mathbb{I}^X$."),
        ).arrange(DOWN, buff=0.4)
        self.play(Write(definition_ivfs))
        self.next_slide()
        self.play(definition_ivfs.animate.to_edge(UP))
        self.next_slide()

        ax = Axes(
            x_range=[0, 10], y_range=[0, 1, 0.25], x_length=6, y_length=4.5,
            axis_config={"include_numbers": True},
            tips=False,
        ).next_to(definition_ivfs, DOWN, buff=0.5)

        a_upper_func = lambda x: 0.05 * np.sin(x) + 0.75
        a_lower_func = lambda x: 0.05 * np.sin(x + 2) + 0.25

        a_upper = ax.plot(a_upper_func, color=BLUE)
        a_lower = ax.plot(a_lower_func, color=BLUE)
        ivfs_a = ax.get_area(a_upper, bounded_graph=a_lower, color=BLUE, opacity=0.4)
        a_label = MathTex("A", color=BLUE).next_to(ivfs_a, RIGHT).shift(UP * 0.3 )

        self.play(Create(ax))
        self.play(Create(ivfs_a), Write(a_label))
        self.next_slide()

        self.play(FadeOut(definition_ivfs))

        embedding_def = VGroup(
            Tex(r"Let $A, B$ be IVFS. The \textbf{embedding relation} $\sqsubseteq$ is defined as:"),
            MathTex(r"B \sqsubseteq A \iff \forall x \in X: B(x) \sqsubseteq A(x)"),
        ).arrange(DOWN, buff=0.4).to_edge(UP)

        self.play(Write(embedding_def))
        self.next_slide()

        b_upper_func = lambda x: 0.05 * np.sin(x + 4) + 0.65
        b_lower_func = lambda x: 0.05 * np.sin(x - 12) + 0.35

        b_upper = ax.plot(b_upper_func, color=RED)
        b_lower = ax.plot(b_lower_func, color=RED)
        ivfs_b = ax.get_area(b_upper, bounded_graph=b_lower, color=RED, opacity=0.6)
        b_label = MathTex("B", color=RED).next_to(ivfs_b, RIGHT).shift(DOWN * 0.3 )

        self.play(Create(ivfs_b), Write(b_label))
        self.next_slide()

        # New slide starts here
        self.play(FadeOut(embedding_def))
        note_text = MathTex(r"\text{Notice that: } \sqsubseteq \neq \subseteq").to_edge(UP)
        self.play(Write(note_text))
        self.next_slide()

        graph_embedding = VGroup(ax, ivfs_a, a_label, ivfs_b, b_label)
        self.play(graph_embedding.animate.scale(0.85).next_to(note_text, DOWN, buff=0.5).shift(LEFT*3.5))
        label_embedding = MathTex(r"B \sqsubseteq A").next_to(graph_embedding, DOWN)
        self.play(Write(label_embedding))

        ax_subset = Axes(
            x_range=[0, 10], y_range=[0, 1, 0.25], x_length=6, y_length=4.5,
            axis_config={"include_numbers": True},
            tips=False,
        ).scale(0.85).next_to(note_text, DOWN, buff=0.5).shift(RIGHT*3.5)

        c_lower_func = lambda x: 0.05 * np.sin(x) + 0.15
        c_upper_func = lambda x: 0.05 * np.sin(x+2) + 0.55
        d_lower_func = lambda x: 0.05 * np.sin(x) + 0.45
        d_upper_func = lambda x: 0.05 * np.sin(x+2) + 0.75

        c_upper = ax_subset.plot(c_upper_func, color=GREEN)
        c_lower = ax_subset.plot(c_lower_func, color=GREEN)
        ivfs_c = ax_subset.get_area(c_upper, bounded_graph=c_lower, color=GREEN, opacity=0.5)
        c_label = MathTex("C", color=GREEN).next_to(ivfs_c, RIGHT)

        d_upper = ax_subset.plot(d_upper_func, color=ORANGE)
        d_lower = ax_subset.plot(d_lower_func, color=ORANGE)
        ivfs_d = ax_subset.get_area(d_upper, bounded_graph=d_lower, color=ORANGE, opacity=0.5)
        d_label = MathTex("D", color=ORANGE).next_to(ivfs_d, RIGHT)

        label_subset = MathTex(r"C \subseteq D").next_to(ax_subset, DOWN)

        self.play(Create(ax_subset))
        self.play(
            Create(ivfs_c), Write(c_label),
            Create(ivfs_d), Write(d_label)
        )
        self.play(Write(label_subset))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING IVFSSimilarityMeasure

class IVFSSimilarityMeasure(Slide):
    def construct(self):
        definition_text = VGroup(
            Tex(r"$S : \mathbb{I}^X \times \mathbb{I}^X \to [0, 1]$ is a similarity measure for"),
            Tex(r"interval-valued fuzzy sets when, $\forall A, B, C \in \mathbb{I}^X$:")
        ).arrange(DOWN).to_edge(UP)

        self.play(Write(definition_text))
        self.next_slide()

        # Properties
        properties = VGroup(
            Tex(r"P1: $S(A, B) = 1 \iff A = B$"),
            Tex(r"P2: $S(A, B) = S(B, A)$"),
            Tex(r"P3: $S(A, A^c) = 0$ if $A$ is a crisp set"),
            Tex(r"P4: $A \sqsubseteq B \sqsubseteq C \implies \begin{gathered} S(A, C) \le S(A, B) \text{ and} \\ S(A, C) \le S(B, C) \end{gathered}$")
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).next_to(definition_text, DOWN, buff=1).to_edge(LEFT)

        for prop in properties:
            self.play(Write(prop))
            self.next_slide()

        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ObjectSimilarityProposition

class ObjectSimilarityProposition(Slide):
    def construct(self):
        definition = VGroup(
            Tex(r"Let $S$ be a similarity measure for intervals, $X=\{x_1, \dots, x_n\}$,"),
            Tex(r"and $\mathbb{S} : \mathbb{I}^X \times \mathbb{I}^X \to [0, 1]$ be defined by:")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(UP)

        self.play(Write(definition))

        eq = MathTex(r"\mathbb{S}(A, B) = \frac{\sum_{k=1}^{n} S(A(x_k), B(x_k))}{n}")
        self.play(Write(eq))

        prop = Tex(r"Then the agregation $\mathbb{S}$ is an IVFS similarity measure.").next_to(eq, DOWN, buff=1).to_edge(LEFT)
        self.play(Write(prop))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))

# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofP1IVFS

class ProofP1IVFS(Slide):
    def construct(self):
        p1_goal = Tex(r"Proof of P1: $\mathbb{S}(A, B) = 1 \iff A=B$").to_edge(UP)
        self.play(Write(p1_goal))

        p1_proof = Tex("Immediate, since $S(A(x_i),B(x_i)) = 1 \iff A(x_i)=B(x_i)$")
        self.play(Write(p1_proof))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofP2IVFS

class ProofP2IVFS(Slide):
    def construct(self):
        p2_goal = Tex(r"Proof of P2: $\mathbb{S}(A, B) = \mathbb{S}(B, A)$").to_edge(UP)
        self.play(Write(p2_goal))

        p2_proof = Tex("Immediate, since S is simmetric.")
        self.play(Write(p2_proof))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofP3IVFS

class ProofP3IVFS(Slide):
    def construct(self):
        p3_goal = Tex(r"Proof of P3: If $A$ is a crisp set, then $\mathbb{S}(A, A^c) = 0$.").to_edge(UP)
        self.play(Write(p3_goal))

        p3_proof = VGroup(
            MathTex(r"\mathbb{S}(A, A^c) = \frac{\sum_{k=1}^{n} S(A(x_k), A^c(x_k))}{n} = 0"),
            Tex(r"as $S(A(x_k), A^c(x_k)) = 0$ for each $x_k$ since $A$ is crisp.")
        ).arrange(DOWN, buff=0.5)

        self.play(Write(p3_proof))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))


# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ProofP4IVFS

class ProofP4IVFS(Slide):
    def construct(self):
        p4_goal_text = r"Proof of P4: $A \sqsubseteq B \sqsubseteq C \implies \begin{gathered} \mathbb{S}(A, C) \le \mathbb{S}(A, B) \text{ and} \\ \mathbb{S}(A, C) \le \mathbb{S}(B, C) \end{gathered}$"
        p4_goal = Tex(p4_goal_text).to_edge(UP)
        self.play(Write(p4_goal))

        proof1_step1 = MathTex(r"\mathbb{S}(A, C) = \frac{\sum_{k=1}^{n} S(A(x_k), C(x_k))}{n}")
        proof1_step2 = MathTex(r"\mathbb{S}(A, C) \le \frac{\sum_{k=1}^{n} S(A(x_k), B(x_k))}{n}")
        proof1_step3 = MathTex(r"\mathbb{S}(A, C) \le \mathbb{S}(A, B)")

        proof1_step1.center()
        self.play(Write(proof1_step1))
        self.next_slide()

        p4_reason_1 = Tex(r"as $S(A(x_k), C(x_k)) \le S(A(x_k), B(x_k))$").next_to(proof1_step1, DOWN)
        proof1_step2.move_to(proof1_step1)
        self.play(Transform(proof1_step1, proof1_step2), Write(p4_reason_1))
        self.next_slide()

        proof1_step3.move_to(proof1_step1)
        self.play(Transform(proof1_step1, proof1_step3))
        self.next_slide()

        proof_group_1 = VGroup(proof1_step1, p4_reason_1)
        self.play(FadeOut(proof_group_1))
        self.next_slide()

        proof2_step1 = MathTex(r"\mathbb{S}(A, C) = \frac{\sum_{k=1}^{n} S(A(x_k), C(x_k))}{n}")
        proof2_step2 = MathTex(r"\mathbb{S}(A, C) \le \frac{\sum_{k=1}^{n} S(B(x_k), C(x_k))}{n}")
        proof2_step3 = MathTex(r"\mathbb{S}(A, C) \le \mathbb{S}(B, C)")

        proof2_step1.center()
        self.play(Write(proof2_step1))
        self.next_slide()

        p4_reason_2 = Tex(r"as $S(A(x_k), C(x_k)) \le S(B(x_k), C(x_k))$").next_to(proof2_step1, DOWN)
        proof2_step2.move_to(proof2_step1)
        self.play(Transform(proof2_step1, proof2_step2), Write(p4_reason_2))
        self.next_slide()

        proof2_step3.move_to(proof2_step1)
        self.play(Transform(proof2_step1, proof2_step3))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))




# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING HierarchicalClusteringAlgorithm

class HierarchicalClusteringAlgorithm(Slide):
    def construct(self):
        title = Tex(r"Hierarchical Clustering Algorithm").to_edge(UP)

        alg_lines = [
            r"1. \textbf{Input:} Dataset $\mathcal{D}=\{A_1, ..., A_m\} \subset \mathbb{I}^n$, interval similarity $S$, linkage $\mu$",
            r"2. Let $\mathbf{M}$ be the $m \times m$ similarity matrix",
            r"3. \textbf{for} each pair $(A_i, A_j)$ in $\mathcal{D}$:",
            r"4. \qquad $\mathbf{M}_{ij} = \mathbb{S}(A_i, A_j) = \frac{\sum_{k=1}^{n} S(A_i^k, A_j^k)}{n}$",
            r"5. \textbf{end for}",
            r"6. Use $\mathbf{M}$ as input for hierarchical clustering with linkage $\mu$",
            r"7. Initially, each object is in its own cluster (leaves of the dendrogram)",
            r"8. \textbf{while} number of clusters $> 1$:",
            r"9. \qquad Find and merge the two closest clusters using $\mu$",
            r"10. \textbf{end while}",
            r"11. \textbf{Output:} Dendrogram"
        ]

        algorithm = VGroup(*[
            Tex(line, tex_environment="flushleft") for line in alg_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.7).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(algorithm))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ExampleWalkthrough

class ExampleWalkthrough(Slide):
    def construct(self):
        # 1. Show initial data table
        title = Tex("Example: Weather Data").to_edge(UP)
        self.play(Write(title))

        raw_data = [
            ["Y", r"\text{Temperature}", r"\text{Precipitation}"],
            ["z_1", "[5,11]", "[16,21]"],
            ["z_2", "[6,12]", "[0,8]"],
            ["z_3", "[7,16]", "[7,30]"],
            ["z_4", "[-1,6]", "[19,50]"],
            ["z_5", "[4,19]", "[4,21]"],
            ["z_6", "[2,11]", "[13,25]"]
        ]
        raw_table = MathTable(raw_data, include_outer_lines=True).scale(0.5)
        self.play(Write(raw_table))
        self.next_slide()

        # 2. Transform to normalized table
        normalized_data = [
            [r"Y^{[0,1]}", r"\text{Temperature}", r"\text{Precipitation}"],
            ["y_1", "[0.3,0.6]", "[0.32,0.42]"],
            ["y_2", "[0.35,0.65]", "[0,0.16]"],
            ["y_3", "[0.4,0.85]", "[0.14,0.6]"],
            ["y_4", "[0,0.35]", "[0.38,1]"],
            ["y_5", "[0.25,1]", "[0.08,0.42]"],
            ["y_6", "[0.15,0.6]", "[0.26,0.5]"]
        ]
        normalized_table = MathTable(normalized_data, include_outer_lines=True).scale(0.5)
        self.play(Transform(raw_table, normalized_table))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))



def create_custom_matrix(top_labels_str, left_labels_str, values_data, color=False):
    # Create the table with labels but make all lines invisible
    table_content = [[""] + top_labels_str] + [[left_labels_str[i]] + values_data[i] for i in range(len(left_labels_str))]
    table = MathTable(table_content, include_outer_lines=False)
    table.get_horizontal_lines().set_stroke(width=0)
    table.get_vertical_lines().set_stroke(width=0)

    # Draw the custom stepped border
    border = VGroup()
    for i in range(len(left_labels_str)):
        for j in range(i, len(top_labels_str)): # Iterate 0<=i<=j
            cell = table.get_cell((i + 2, j + 2)) # +2 for labels

            # Top border for the first row
            if i == 0:
                border.add(Line(cell.get_corner(UL), cell.get_corner(UR)))
            # Right border for the last column
            if j == len(top_labels_str) - 1:
                border.add(Line(cell.get_corner(UR), cell.get_corner(DR)))
            # Left and Bottom for the diagonal
            if i == j:
                border.add(Line(cell.get_corner(DL), cell.get_corner(DR)))
                border.add(Line(cell.get_corner(UL), cell.get_corner(DL)))

    matrix_group = VGroup(table, border)
    return matrix_group



# Commented out IPython magic to ensure Python compatibility.
# %%manim -ql -v WARNING ExampleWalkthroughPart2

class ExampleWalkthroughPart2(Slide):
    def construct(self):
        temp_values = [
            ["0.8333", "0.5556", "0.1548", "0.7", "0.8333"],
            ["", "0.6944", "0", "0.7", "0.6944"],
            ["", "", "0", "0.8", "0.4444"],
            ["", "", "", "0.2095", "0.5079"],
            ["", "", "", "", "0.6222"]
        ]
        temp_group = create_custom_matrix(["y_2", "y_3", "y_4", "y_5", "y_6"], ["y_1", "y_2", "y_3", "y_4", "y_5"], temp_values).scale(0.45)
        temp_title = Tex("Temperature")
        temp = VGroup(temp_title, temp_group).arrange(DOWN)

        precip_values = [
            ["0", "0.6087", "0.2323", "0.6470", "0.7083"],
            ["", "0.0842", "0", "0.3676", "0"],
            ["", "", "0.4165", "0.7161", "0.7609"],
            ["", "", "", "0.0910", "0.3468"],
            ["", "", "", "", "0.5687"]
        ]
        precip_group = create_custom_matrix(["y_2", "y_3", "y_4", "y_5", "y_6"], ["y_1", "y_2", "y_3", "y_4", "y_5"], precip_values).scale(0.45)
        precip_title = Tex("Preciptation")
        precip = VGroup(precip_title, precip_group).arrange(DOWN)

        both = VGroup(temp, precip).arrange(RIGHT).center()
        self.play(Create(both))
        self.next_slide()

        # 4. Merge matrices
        aggregated_matrix_data = [
            ["0.4167", "0.5821", "0.1935", "0.6735", "0.7708"],
            ["", "0.3893", "0", "0.5338", "0.3472"],
            ["", "", "0.2083", "0.7581", "0.6027"],
            ["", "", "", "0.1503", "0.4274"],
            ["", "", "", "", "0.5955"]
        ]
        aggregated_matrix = create_custom_matrix(["y_2", "y_3", "y_4", "y_5", "y_6"], ["y_1", "y_2", "y_3", "y_4", "y_5"], aggregated_matrix_data, True).scale(0.7)
        aggregated_title = Tex(r"Aggregated Similarity $\mathbb{S}$")
        aggregated_group = VGroup(aggregated_title, aggregated_matrix).arrange(DOWN).center()

        self.play(ReplacementTransform(precip, aggregated_group), ReplacementTransform(temp, aggregated_group))
        self.next_slide()
        self.play(aggregated_group.animate.scale(0.8), FadeOut(aggregated_title))
        self.play(aggregated_matrix.animate.to_edge(LEFT))


        # Setup Leaves
        leaf_labels_str = [r"y_4", r"y_2", r"y_1", r"y_6", r"y_3", r"y_5"]
        leaf_mobs = VGroup(*[MathTex(label) for label in leaf_labels_str]).arrange(RIGHT, buff=0.4)

        # Position leaves at the bottom of the screen
        leaf_mobs.to_corner(DR)

        base_line_y = leaf_mobs.get_y()

        self.play(FadeIn(leaf_mobs))
        self.next_slide()

        # Define leaf positions using the mobjects, adding a small buffer
        leaf_pos = {
            label: mob.get_top() + UP * 0.2 for label, mob in zip(leaf_labels_str, leaf_mobs)
        }

        # Function to draw a merge
        def draw_merge(cluster_name_left, cluster_name_right, height):
            y_scale_factor = 8 # Scales dissimilarity value to screen units

            pos_left = leaf_pos[cluster_name_left]
            pos_right = leaf_pos[cluster_name_right]

            x1 = pos_left[0]
            x2 = pos_right[0]
            y_height = base_line_y + height * y_scale_factor

            # Vertical lines from current position up to the merge height
            line_left = Line(pos_left, [x1, y_height, 0])
            line_right = Line(pos_right, [x2, y_height, 0])

            # Horizontal line connecting the vertical lines
            line_horizontal = Line([x1, y_height, 0], [x2, y_height, 0])

            # Update leaf_pos for the new merged cluster (at the center of the horizontal line)
            new_cluster_name = f"({cluster_name_left},{cluster_name_right})"
            leaf_pos[new_cluster_name] = line_horizontal.get_center()

            return VGroup(line_left, line_right, line_horizontal)

        # Merge 1: (y_3, y_5) at ~0.25
        merge1 = draw_merge(r"y_3", r"y_5", 0.25)
        self.play(Create(merge1))
        self.next_slide()

        # Merge 2: (y_1, y_6) at ~0.25
        merge2 = draw_merge(r"y_1", r"y_6", 0.25)
        self.play(Create(merge2))
        self.next_slide()

        # Merge 3: ((y_1,y_6),(y_3,y_5)) at ~0.35
        merge3 = draw_merge("(y_1,y_6)", "(y_3,y_5)", 0.35)
        self.play(Create(merge3))
        self.next_slide()

        # Merge 4: (y_2, ((y_1,y_6),(y_3,y_5))) at ~0.5
        merge4 = draw_merge("y_2", "((y_1,y_6),(y_3,y_5))", 0.5)
        self.play(Create(merge4))
        self.next_slide()

        # Merge 5: (y_4, (y_2, ((y_1,y_6),(y_3,y_5)))) at ~0.6
        merge5 = draw_merge("y_4", "(y_2,((y_1,y_6),(y_3,y_5)))", 0.6)
        self.play(Create(merge5))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
