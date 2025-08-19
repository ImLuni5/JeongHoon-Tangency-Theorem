from manim import *
import math

config.disable_caching = True

class Video(Scene):
    def construct(self):
        self.add_sound("bgm.mp3", gain=-40)
        self.add_sound("접1.m4a")
        title_main = Text("JeongHoon Tangency Theorem", font_size=48)
        title_main.set_color(BLUE_B)
        self.play(Write(title_main))
        self.wait()
        self.play(title_main.animate.to_edge(UP, buff=1))

        theorem1 = MathTex(r" f(x),\; \frac{f(x)}{g(x)}", font_size=32)
        theorem2 = MathTex(r"g(t)=1,\; f(t)g'(t)=0", font_size=48)

        theorem2.next_to(theorem1, DOWN, buff=0.5)

        self.play(Write(theorem1))
        self.wait(4)
        self.play(Write(theorem2))
        self.wait()
        self.add_sound("접2.m4a")
        self.play(Unwrite(theorem1), theorem2.animate.to_edge(DOWN))
        self.wait()

        proof1 = MathTex(r"f(x)=\frac{f(x)}{g(x)}", font_size=32)
        proof2 = MathTex(r"f'(x)=\frac{f'(x)g(x)-f(x)g'(x)}{\begin{Bmatrix}g(x)\end{Bmatrix}^2}", font_size=32)
        proof3 = MathTex(r"f'(x)=f'(x)", font_size=32)

        self.play(Write(proof1))
        self.wait()
        self.play(Transform(proof1, proof2))
        self.wait(2)
        self.play(Circumscribe(theorem2, color=YELLOW, run_time=2))
        self.play(Transform(proof1, proof3))
        self.wait()
        self.add_sound("접3_1.m4a")
        self.play(Unwrite(proof1), Unwrite(theorem2))
        self.wait(3)
        self.add_sound("접3_2.m4a")

        gText = MathTex(r"g(x)=1+\operatorname{sin}^2f(x)", font_size=32, color=BLUE)
        self.play(Write(gText))
        self.wait(5)
        self.add_sound("접3_3.m4a")
        self.play(gText.animate.to_edge(DOWN))

        fText = MathTex(r"f(x)=e^x", font_size=32, color=RED)
        fText.next_to(gText, UP)
        self.play(Write(fText))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-10, 10, 2],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True},
        )
        axes.shift(DOWN*2)
        axes.y_axis.set_opacity(0)
        axes.z_index = -1

        # 함수 정의
        def f(x):
            return math.exp(x)

        def g(x):
            return 1+math.sin(x)**2

        def h(x):  # f(x)/g(x)
            try:
                return f(x) / g(f(x))
            except ZeroDivisionError:
                return float('inf')

        # 그래프 생성
        graph_f = axes.plot(f, color=RED, x_range=[-5, 5])
        graph_h = axes.plot(h, color=PURPLE, x_range=[-5, 5])
        graph_f.z_index = -1
        graph_h.z_index = -1

        # 씬에 추가
        self.play(Create(axes), Create(graph_f), Create(graph_h))
        self.wait(3)

        fText2 = MathTex(r"f(x)=x^3", font_size=32, color=RED)
        fText2.next_to(gText, UP)

        def f2(x):
            return x**3

        def h2(x):  # f(x)/g(x)
            try:
                return f2(x) / g(f2(x))
            except ZeroDivisionError:
                return float('inf')

        graph_f2 = axes.plot(f2, color=RED, x_range=[-5, 5])
        graph_h2 = axes.plot(h2, color=PURPLE, x_range=[-5, 5])
        graph_f2.z_index = -1
        graph_h2.z_index = -1
        self.add_sound("접4.wav")

        self.play(Transform(fText, fText2), Transform(graph_f, graph_f2), Transform(graph_h, graph_h2))
        self.wait(4.5)

        fText3 = MathTex(r"f(x)=e^{\operatorname{sin}x}\operatorname{ln}x", font_size=32, color=RED)
        fText3.next_to(gText, UP)

        axes2 = Axes(
            x_range=[0, 50, 5],
            y_range=[-10, 10, 2],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True},
        )
        axes2.shift(DOWN*2)
        axes2.y_axis.set_opacity(0)
        axes2.z_index = -1

        def f3(x):
            return math.exp(math.sin(x))*math.log(x)

        def h3(x):  # f(x)/g(x)
            try:
                return f3(x) / g(f3(x))
            except ZeroDivisionError:
                return float('inf')

        graph_f3 = axes2.plot(f3, color=RED, x_range=[0.1, 50])
        graph_h3 = axes2.plot(h3, color=PURPLE, x_range=[0.1, 50])
        graph_f3.z_index = -1
        graph_h3.z_index = -1

        self.add_sound("접5.m4a")
        self.play(Transform(axes, axes2), Transform(fText, fText3), Transform(graph_f, graph_f3), Transform(graph_h, graph_h3))
        self.wait(16)

        self.add_sound("접6.m4a")
        self.wait(6)
        gText2 = MathTex(r"g(x)=|\operatorname{sec}kx|", font_size=32, color=BLUE)
        gText2.to_edge(DOWN)
        self.play(Transform(gText, gText2), Uncreate(graph_f), Uncreate(graph_h))
        self.wait(2)

        def f4(x):
            return math.log(x)
        def g2(x, k):
            try:
                return abs(1 / math.cos(k * x))
            except:
                return float('inf')

        def h4(x, k):  # f(x)/g(x)
            try:
                return f4(x) / g2(f4(x), k)
            except ZeroDivisionError:
                return float('inf')
            
        k_tracker = ValueTracker(1)

        def manual_plot(f, x_range, color=RED, n_samples=1000):
            x_min, x_max = x_range
            dx = (x_max - x_min) / n_samples
            points = []

            for i in range(n_samples + 1):
                x = x_min + i * dx
                try:
                    y = f(x)
                    if not math.isfinite(y):  # inf, nan 제외
                        continue
                    points.append(axes2.c2p(x, y))
                except:
                    continue

            graph = VMobject()
            if points:
                graph.set_points_smoothly(points)
                graph.set_color(color)
            return graph

        graph_h4 = always_redraw(lambda: manual_plot(
            lambda x: h4(x, k_tracker.get_value()),
            x_range=[0.1, 50],
            color=PURPLE,
            n_samples=3000  # 여기서 원하는 해상도로 늘려
        ))

            
        graph_f4 = axes2.plot(f4, color=RED, x_range=[0.1, 50])
        graph_f4.z_index = -1
        graph_h4.z_index = -1

        gText3 = always_redraw(lambda: MathTex(
            rf"g(x) = \left|\sec\left({k_tracker.get_value():.2f}x\right)\right|",
            font_size=32, color=BLUE
        ).to_edge(DOWN))

        fText4 = MathTex(r"f(x)=\operatorname{ln}x", font_size=32, color=RED)
        fText4.next_to(gText, UP)

        self.remove(gText)
        self.add(gText3)
        self.play(Create(graph_f4), Create(graph_h4), Transform(fText, fText4))
        self.wait()
        self.add_sound("접7.m4a")
        self.wait(3)
        self.play(k_tracker.animate.set_value(100), run_time=4)
        self.wait(4)

        integral = MathTex(r" \int f(x)dx?", font_size=32).next_to(graph_f4, UP, buff=0.5)
        self.play(Write(integral))
        self.wait()
        self.add_sound("접8.m4a")

        infL = MathTex(r"\lim_{k \to \infty}L_k", font_size=32)
        self.play(Uncreate(axes), Unwrite(integral), Unwrite(gText3), Unwrite(fText), Uncreate(graph_f4), Uncreate(graph_h4))
        self.wait()
        self.play(Write(infL))
        self.wait(4)
        infL2 = MathTex(r"\lim_{k \to \infty}L_k \cdot h(k) = \int_{a}^{b}f(x)dx", font_size=32)
        self.play(Transform(infL, infL2))
        self.wait(6)
        self.play(Unwrite(infL))
        self.wait()

        define1 = MathTex(r"y_k(x)=\frac{f(x)}{|\operatorname{sec}kx|}=f(x)|\operatorname{cos}kx|", font_size=32)
        define2 = MathTex(r"L_k=\int_{a}^{b}\sqrt{1+\begin{Bmatrix}y_k'(x)\end{Bmatrix}^2}dx", font_size=32).next_to(define1, DOWN, buff=0.5)

        self.add_sound("접9.m4a")
        self.play(Write(define1), Write(define2))
        self.wait(2)
        self.play(Unwrite(define1), Unwrite(define2))
        self.wait()

        diffy = MathTex(r"y_k'(x)=f'(x)|\cos{kx}|+f(x)\frac{d}{dx}|\cos{kx}|", font_size=32)
        diffcos = MathTex(r"\frac{d}{dx}|\cos{kx}|=-k\sin{kx}\operatorname{sgn}(\cos{kx})", font_size=32).next_to(diffy, DOWN, buff=0.5)
        diffy2 = MathTex(r"y_k'(x)=f'(x)|\cos{kx}|-kf'(x)\sin{kx}\operatorname{sgn}(\cos{kx})", font_size=32)

        self.add_sound("접10.m4a")
        self.play(Write(diffy))
        self.wait()
        self.add_sound("접11.m4a")
        self.play(Write(diffcos))
        self.wait(1.5)
        self.play(Circumscribe(diffcos, color=YELLOW, run_time=2))
        self.play(ReplacementTransform(diffcos, diffy),Transform(diffy, diffy2))
        self.wait()
        self.play(Unwrite(diffy))
        self.wait()

        self.add_sound("접12_1.m4a")
        Lk = MathTex(r"L_k=\int_{a}^{b}\sqrt{1+(f'(x)|\cos{kx}|)^2-2k|\cos{kx}|f'(x)f(x)\sin{kx}\operatorname{sgn}(\cos{kx})+",r"k^2\begin{Bmatrix}f(x)\end{Bmatrix}^2\sin^2{kx}}", r"dx", font_size=32)
        self.play(Write(Lk))
        self.wait(6)
        self.add_sound("접12_2.m4a")
        self.play(Circumscribe(Lk[1], color=YELLOW, run_time=2))
        self.wait(5)

        Lk2 = MathTex(r"L_k\sim \int_{a}^{b}{kf(x)",r"|\sin{kx}|}",r"dx", font_size=32)
        self.play(Transform(Lk, Lk2))
        self.wait(5.5)
        self.add_sound("접13.m4a")
        self.wait(1.5)
        self.play(Circumscribe(Lk2[1], color=YELLOW, run_time=2))
        self.wait(8)
        
        dL = MathTex(r"\Delta L_j\sim \int_{x_j}^{x_j+\frac{2\pi}{k}}{kf(x)|\sin{kx}|}dx", font_size=32)
        self.play(Transform(Lk, dL))
        self.add_sound("접14.m4a")
        sim = MathTex(r"f(x_j)\sim f(x_j+\frac{2\pi}{k})", font_size=32).next_to(dL, DOWN, buff=0.5)
        self.play(Write(sim))
        self.wait(2)
        dL2 = MathTex(r"\Delta L_j\sim kf(x_j)",r"\int_{x_j}^{x_j+\frac{2\pi}{k}}{|\sin{kx}|}dx", font_size=32)
        self.play(Transform(Lk, dL2), Unwrite(sim))
        self.wait()

        self.add_sound("접15.m4a")
        self.play(Circumscribe(dL2[1], color=YELLOW, run_time=2))
        self.wait(7)
        dL3 = MathTex(r"\Delta L_j\sim kf(x_j) \cdot \frac{4}{k}", font_size=32)
        self.play(Transform(Lk, dL3))
        self.wait()
        
        self.add_sound("접16.m4a")
        N = MathTex(r"N=\frac{b-a}{\frac{2\pi}{k}}=\frac{k(b-a)}{2\pi}", font_size=32).next_to(dL3, DOWN, buff=0.5)
        self.play(Write(N))
        self.wait(1.5)
        final = MathTex(r"\lim_{k \to \infty}L_k=\lim_{k \to \infty}4\sum_{j=1}^{N}f(x_j)", font_size=32)
        self.play(Transform(Lk, final))
        self.play(Unwrite(N))
        self.wait(3.5)

        self.add_sound("접17.m4a")
        self.wait(2.5)
        dx = MathTex(r"\Delta x=\frac{2\pi}{k}", font_size=32).next_to(final, DOWN, buff=0.5)
        self.play(Write(dx))
        self.wait(2)
        final2 = MathTex(r"\lim_{k \to \infty}\frac{\pi}{2k}L_k=\lim_{k \to \infty}\sum_{j=1}^{N}f(x_j)\Delta x", font_size=32)
        self.play(Transform(Lk, final2))
        self.play(Unwrite(dx))
        self.wait()
        final3 = MathTex(r"\lim_{k \to \infty}\frac{\pi}{2k}L_k=\int_{a}^{b}f(x)dx", font_size=32)
        self.play(Transform(Lk, final3))
        self.wait(0.5)
        self.add_sound("접18.m4a")
