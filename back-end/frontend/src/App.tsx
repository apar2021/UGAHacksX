import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import { Button } from "./components/ui/button"
import Login from "./pages/Login"
import Register from "./pages/Register"

function Home() {
  return (
    <div className="min-h-screen bg-background">
      <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-14 items-center">
          <div className="mr-4 flex">
            <Link to="/" className="mr-6 flex items-center space-x-2">
              <span className="font-bold">Sound Sync</span>
            </Link>
            <nav className="flex items-center space-x-6 text-sm font-medium">
              <Link to="/about" className="transition-colors hover:text-foreground/80 text-foreground/60">
                About
              </Link>
              <Link to="/login" className="transition-colors hover:text-foreground/80 text-foreground/60">
                Login
              </Link>
              <Link to="/register" className="transition-colors hover:text-foreground/80 text-foreground/60">
                Register
              </Link>
            </nav>
          </div>
        </div>
      </header>
      <main className="flex-1">
        <section className="space-y-6 pb-8 pt-6 md:pb-12 md:pt-10 lg:py-32">
          <div className="container flex max-w-[64rem] flex-col items-center gap-4 text-center">
            <h1 className="font-heading text-3xl sm:text-5xl md:text-6xl lg:text-7xl">
              Find Your Perfect Sound Match
            </h1>
            <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-xl sm:leading-8">
              Connect with musicians who share your passion and style. Create, collaborate, and make music together.
            </p>
            <div className="space-x-4">
              <Link to="/register">
                <Button size="lg">Get Started</Button>
              </Link>
              <Link to="/about">
                <Button variant="outline" size="lg">
                  Learn More
                </Button>
              </Link>
            </div>
          </div>
        </section>
        <section className="container space-y-6 py-8 md:py-12 lg:py-24">
          <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
            <h2 className="font-heading text-3xl leading-[1.1] sm:text-3xl md:text-6xl">
              Features
            </h2>
            <p className="max-w-[85%] leading-normal text-muted-foreground sm:text-lg sm:leading-7">
              Everything you need to find and connect with your perfect musical match.
            </p>
          </div>
          <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3 lg:gap-8">
            <div className="relative overflow-hidden rounded-lg border bg-background p-2">
              <div className="flex h-[180px] flex-col justify-between rounded-md p-6">
                <div className="space-y-2">
                  <h3 className="font-bold">Smart Matching</h3>
                  <p className="text-sm text-muted-foreground">
                    Our algorithm matches you with musicians based on your musical preferences and style.
                  </p>
                </div>
              </div>
            </div>
            <div className="relative overflow-hidden rounded-lg border bg-background p-2">
              <div className="flex h-[180px] flex-col justify-between rounded-md p-6">
                <div className="space-y-2">
                  <h3 className="font-bold">Profile Creation</h3>
                  <p className="text-sm text-muted-foreground">
                    Create a detailed profile showcasing your musical journey, skills, and aspirations.
                  </p>
                </div>
              </div>
            </div>
            <div className="relative overflow-hidden rounded-lg border bg-background p-2">
              <div className="flex h-[180px] flex-col justify-between rounded-md p-6">
                <div className="space-y-2">
                  <h3 className="font-bold">Messaging</h3>
                  <p className="text-sm text-muted-foreground">
                    Connect and communicate with potential collaborators through our built-in messaging system.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer className="border-t py-6 md:py-0">
        <div className="container flex flex-col items-center justify-between gap-4 md:h-24 md:flex-row">
          <div className="flex flex-col items-center gap-4 px-8 md:flex-row md:gap-2 md:px-0">
            <p className="text-center text-sm leading-loose text-muted-foreground md:text-left">
              Built by the Sound Sync Team. The source code is available on{" "}
              <a
                href="https://github.com/yourusername/sound-sync"
                target="_blank"
                rel="noreferrer"
                className="font-medium underline underline-offset-4"
              >
                GitHub
              </a>
              .
            </p>
          </div>
        </div>
      </footer>
    </div>
  )
}

function About() {
  return (
    <div className="min-h-screen bg-background">
      <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-14 items-center">
          <div className="mr-4 flex">
            <Link to="/" className="mr-6 flex items-center space-x-2">
              <span className="font-bold">Sound Sync</span>
            </Link>
            <nav className="flex items-center space-x-6 text-sm font-medium">
              <Link to="/about" className="transition-colors hover:text-foreground/80 text-foreground/60">
                About
              </Link>
              <Link to="/login" className="transition-colors hover:text-foreground/80 text-foreground/60">
                Login
              </Link>
              <Link to="/register" className="transition-colors hover:text-foreground/80 text-foreground/60">
                Register
              </Link>
            </nav>
          </div>
        </div>
      </header>
      <main className="container py-8">
        <h1 className="text-4xl font-bold mb-6">About Sound Sync</h1>
        <p className="text-lg text-muted-foreground mb-4">
          Sound Sync is a platform designed to connect musicians and help them find their perfect musical match.
          Whether you're a solo artist looking for a band, a producer seeking vocalists, or just want to jam with
          like-minded musicians, we've got you covered.
        </p>
        <p className="text-lg text-muted-foreground">
          Our mission is to make it easier for musicians to find collaborators and create amazing music together.
          We believe that great music comes from great connections, and we're here to help you make those connections.
        </p>
      </main>
    </div>
  )
}

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  )
}
