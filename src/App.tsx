import { motion } from 'framer-motion';
import { Rocket, Zap, Shield, Globe, Terminal, Code2, ArrowRight, Github, Send, Layers, Cpu, Database } from 'lucide-react';

const Features = [
    {
        icon: <Zap className="w-6 h-6 text-flask" />,
        title: "Ultra-Fast Routing",
        description: "Built on top of a highly optimized internal engine for sub-millisecond route resolution."
    },
    {
        icon: <Shield className="w-6 h-6 text-flask" />,
        title: "Auto-Security",
        description: "Zero-config protection against XSS, CSRF, and SQL injection out of the box."
    },
    {
        icon: <Globe className="w-6 h-6 text-flask" />,
        title: "Global CDN Edge",
        description: "Deploy your Python APIs globally with one click and edge-cached responses."
    }
];

const Stats = [
    { label: "Request/Sec", value: "250K+" },
    { label: "Cold Start", value: "< 12ms" },
    { label: "Uptime", value: "99.99%" }
];

export default function App() {
    return (
        <div className="min-h-screen">
            {/* Background Decor */}
            <div className="fixed inset-0 overflow-hidden pointer-events-none -z-10">
                <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-flask/10 blur-[120px] rounded-full" />
                <div className="absolute bottom-[10%] right-[-5%] w-[30%] h-[30%] bg-blue-600/5 blur-[100px] rounded-full" />
            </div>

            {/* Navigation */}
            <nav className="border-b border-white/5 bg-[#0a192f]/50 backdrop-blur-xl sticky top-0 z-50">
                <div className="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
                    <div className="flex items-center gap-3 group cursor-pointer">
                        <div className="p-2 bg-flask/20 rounded-lg group-hover:bg-flask/30 transition-colors">
                            <Rocket className="w-6 h-6 text-flask" />
                        </div>
                        <span className="text-xl font-bold tracking-tight text-white uppercase tracking-widest">Flask<span className="text-flask">Hub</span></span>
                    </div>

                    <div className="hidden md:flex items-center gap-10">
                        {['Runtime', 'Engine', 'Docs', 'Pricing'].map((item) => (
                            <a key={item} href="#" className="text-xs font-bold uppercase tracking-widest hover:text-flask transition-colors">{item}</a>
                        ))}
                    </div>

                    <button className="px-6 py-2.5 bg-flask text-[#0a192f] font-black text-xs uppercase tracking-widest rounded-full hover:scale-105 transition-transform shadow-neon-strong">
                        Get Trial
                    </button>
                </div>
            </nav>

            <main className="max-w-7xl mx-auto px-6">
                {/* Hero */}
                <section className="py-24 grid lg:grid-cols-2 gap-16 items-center">
                    <motion.div
                        initial={{ opacity: 0, x: -30 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ duration: 0.8 }}
                    >
                        <div className="inline-flex items-center gap-2 px-4 py-2 glass-panel mb-8">
                            <span className="relative flex h-2 w-2">
                                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-flask opacity-75"></span>
                                <span className="relative inline-flex rounded-full h-2 w-2 bg-flask"></span>
                            </span>
                            <span className="text-[10px] uppercase font-bold tracking-widest">Now supporting Async v.4.2</span>
                        </div>

                        <h1 className="text-6xl md:text-[5rem] font-black text-white leading-[0.9] mb-8 uppercase italic tracking-tighter">
                            Accelerate your <br />
                            <span className="text-flask">Backend</span> <br />
                            Performance.
                        </h1>

                        <p className="text-lg text-slate-400 max-w-lg mb-12 leading-relaxed font-medium">
                            The high-performance API hub for Python developers who demand extreme speed, rock-solid security, and instant global scale.
                        </p>

                        <div className="flex flex-col sm:flex-row gap-6">
                            <button className="px-10 py-5 bg-flask text-[#0a192f] font-black rounded-2xl flex items-center justify-center gap-3 hover:shadow-flask/20 hover:shadow-2xl transition-all group">
                                Deploy API <Send className="w-4 h-4 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
                            </button>
                            <button className="px-10 py-5 glass-panel text-white font-black rounded-2xl hover:bg-white/10 transition-colors flex items-center justify-center gap-3 border border-white/10 hover:border-flask/50">
                                <Terminal className="w-4 h-4" /> View Docs
                            </button>
                        </div>
                    </motion.div>

                    {/* Terminal / Code Card */}
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ duration: 0.8, delay: 0.2 }}
                        className="hidden lg:block relative"
                    >
                        <div className="glass-panel p-2 neon-border overflow-hidden">
                            <div className="flex gap-2 p-3 border-b border-white/5">
                                <div className="w-3 h-3 rounded-full bg-red-500/50" />
                                <div className="w-3 h-3 rounded-full bg-yellow-500/50" />
                                <div className="w-3 h-3 rounded-full bg-emerald-500/50" />
                            </div>
                            <div className="p-8 font-mono text-sm leading-relaxed overflow-x-auto whitespace-nowrap">
                                <div className="mb-4 text-slate-500"># main.py</div>
                                <div><span className="text-flask">from</span> flask_hub <span className="text-flask">import</span> Flask, API</div>
                                <div>&nbsp;</div>
                                <div>app = Flask(__name__)</div>
                                <div>api = API(app, version=<span className="text-emerald-400">"v4.0"</span>)</div>
                                <div>&nbsp;</div>
                                <div><span className="text-flask">@api.route</span>(<span className="text-emerald-400">'/v1/metrics'</span>)</div>
                                <div><span className="text-flask">async def</span> <span className="text-emerald-400">get_metrics</span>():</div>
                                <div>&nbsp;&nbsp;&nbsp;&nbsp;stats = <span className="text-flask">await</span> api.get_telemetry()</div>
                                <div>&nbsp;&nbsp;&nbsp;&nbsp;<span className="text-flask">return</span> stats</div>
                                <div>&nbsp;</div>
                                <div className="text-slate-500">// Processing metrics in 0.04ms</div>
                            </div>
                        </div>

                        {/* Floating Card */}
                        <div className="absolute -bottom-10 -left-10 glass-panel p-6 neon-border bg-[#0a192f]/80 animate-bounce group cursor-pointer">
                            <div className="flex items-center gap-4 mb-2">
                                <div className="p-2 bg-emerald-400/20 rounded-full">
                                    <Check className="w-4 h-4 text-emerald-400" />
                                </div>
                                <span className="text-xs font-bold uppercase tracking-widest text-white">SSL Verified</span>
                            </div>
                            <div className="text-[10px] text-slate-500 font-mono tracking-tighter">Endpoint: api.flaskhub.co/v4/auth</div>
                        </div>
                    </motion.div>
                </section>

                {/* Stats */}
                <section className="py-20 border-y border-white/5 mb-32">
                    <div className="grid md:grid-cols-3 gap-12">
                        {Stats.map((stat, i) => (
                            <div key={i} className="text-center group">
                                <div className="text-4xl font-black text-white mb-2 group-hover:text-flask transition-colors">{stat.value}</div>
                                <div className="text-xs font-bold uppercase tracking-[0.3em] text-slate-500">{stat.label}</div>
                            </div>
                        ))}
                    </div>
                </section>

                {/* Features */}
                <section className="py-20 mb-32">
                    <div className="text-center mb-20">
                        <h2 className="text-3xl font-black text-white uppercase tracking-tighter mb-4 italic">Core Engine <span className="text-flask">Components</span></h2>
                        <div className="w-20 h-1 bg-flask mx-auto" />
                    </div>

                    <div className="grid md:grid-cols-3 gap-8">
                        {Features.map((f, i) => (
                            <div key={i} className="glass-panel p-10 hover:border-flask/30 transition-all group">
                                <div className="mb-6 p-4 rounded-2xl bg-white/5 inline-block group-hover:scale-110 transition-transform">
                                    {f.icon}
                                </div>
                                <h3 className="text-xl font-bold text-white mb-4 uppercase tracking-tight">{f.title}</h3>
                                <p className="text-slate-400 text-sm leading-relaxed">{f.description}</p>
                            </div>
                        ))}
                    </div>
                </section>

                {/* Call to Action */}
                <section className="mb-32">
                    <div className="glass-panel p-16 text-center relative overflow-hidden group">
                        <div className="absolute top-0 right-0 p-20 bg-flask/10 blur-[80px] rounded-full group-hover:scale-125 transition-transform" />
                        <h2 className="text-4xl md:text-5xl font-black text-white mb-8 uppercase italic leading-none">Ready to Scale your <br /> <span className="text-flask underline decoration-flask/30 underline-offset-8">Production</span> Infrastructure?</h2>
                        <p className="text-slate-400 max-w-lg mx-auto mb-10 text-lg">Join 15,000+ teams who build on FlaskHub for their most critical API workloads.</p>
                        <div className="flex flex-col sm:flex-row gap-4 justify-center">
                            <button className="px-12 py-5 bg-flask text-[#0a192f] font-black rounded-2xl uppercase text-xs tracking-widest hover:scale-105 transition-transform">Start Building Now</button>
                            <button className="px-12 py-5 glass-panel text-white font-black rounded-2xl border border-white/10 hover:bg-white/5 transition-all flex items-center justify-center gap-3"><Github className="w-5 h-5" /> Fork on GitHub</button>
                        </div>
                    </div>
                </section>
            </main>

            {/* Footer */}
            <footer className="border-t border-white/5 py-16">
                <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-10">
                    <div className="flex items-center gap-3 opacity-50">
                        <Rocket className="w-5 h-5 text-flask" />
                        <span className="text-sm font-bold tracking-tight text-white uppercase tracking-widest">FlaskHub</span>
                    </div>
                    <p className="text-[10px] font-bold text-slate-500 uppercase tracking-[0.4em]">© 2026 FLASK_HUB // ENGINE • 23/30 DISPATCHED</p>
                </div>
            </footer>
        </div>
    );
}

function Check({ className }: { className?: string }) {
    return (
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={3} stroke="currentColor" className={className}>
            <path strokeLinecap="round" strokeLinejoin="round" d="m4.5 12.75 6 6 9-13.5" />
        </svg>
    );
}
