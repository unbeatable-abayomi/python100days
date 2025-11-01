#functions

# Absolutely! This is a great question — and it’s an important one if you're working with **Kubernetes** or **container orchestration** in general.

# Let’s break it down simply and clearly:

# ---

# ## 🎯 High-Level Overview

# | Concept                               | What it does                                                      | Think of it like...                           |
# | ------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------- |
# | **kube-proxy**                        | Manages **networking** for Kubernetes services                    | A traffic controller for your Kubernetes pods |
# | **Container Runtime Interface (CRI)** | Allows Kubernetes to **run containers** (like Docker, containerd) | The engine that actually runs your containers |

# ---

# ## 🧱 What is kube-proxy?

# ### 🔧 kube-proxy: The Network Traffic Router in Kubernetes

# * It's a **Kubernetes component** that runs on **each node** in the cluster.
# * It handles **routing network traffic** **from inside or outside the cluster** to the **correct pod**.
# * It makes **Kubernetes Services** work — especially `ClusterIP`, `NodePort`, and `LoadBalancer`.

# ### 🧠 What it really does:

# * Watches Kubernetes for **new Services and Endpoints**
# * Updates the node's **iptables** or **IPVS rules** (depending on mode)
# * Ensures traffic to a Service is **load-balanced** across the matching pods

# ### 💡 Real-world analogy:

# Imagine your cluster is a hotel.

# * **Each pod** is a hotel room.
# * **kube-proxy** is the **concierge** who knows which guests (users/services) are trying to reach which rooms (pods), and **routes traffic correctly**.

# ---

# ## ⚙️ What is the Container Runtime Interface (CRI)?

# ### 🔧 CRI: The Bridge Between Kubernetes and Containers

# * It’s an **API specification** (not a program) used by Kubernetes to **talk to container runtimes**.
# * Kubernetes itself **doesn’t run containers directly** — it uses a **runtime**, and the CRI tells it **how to talk to** that runtime.

# ### 🧠 The actual container runtime could be:

# * **containerd**
# * **CRI-O**
# * (Previously) **Docker** (via `dockershim`, now deprecated)
# * Others that implement CRI

# ### 💡 Real-world analogy:

# Think of the **container runtime** as the **engine** in your car — it does the heavy lifting (running containers).
# The **CRI** is the **interface (dashboard, pedals, steering wheel)** that lets you control that engine through Kubernetes.

# ---

# ## 🆚 kube-proxy vs CRI — Summary

# | Feature/Aspect          | kube-proxy                       | Container Runtime Interface (CRI)            |
# | ----------------------- | -------------------------------- | -------------------------------------------- |
# | Purpose                 | Manages **network traffic**      | Runs and manages **containers**              |
# | Lives on                | Each Kubernetes node             | Each Kubernetes node (via container runtime) |
# | Used by                 | Kubernetes Services              | kubelet (Kubernetes agent on each node)      |
# | Key function            | Load balances and routes traffic | Starts/stops containers, manages images      |
# | Talks to                | iptables/IPVS, network stack     | container runtimes like containerd or CRI-O  |
# | Does it run containers? | ❌ No                             | ✅ Yes                                        |

# ---

# ## 📌 TL;DR

# * **kube-proxy** is about **networking and routing traffic** to the right pod.
# * **CRI** is about **running containers** using a runtime like containerd.
# * They are both essential but solve **completely different problems** in Kubernetes.

# ---

# Let me know if you want to see an architecture diagram or how they interact in real clusters.

def greet(name):
    print(f"Hello, {name}!")        
greet("Alice")
greet("Bob")

def add(a, b):
    return a + b

result = add(5, 3)


# Hurdle =1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

numbers_of_jump = 6
while numbers_of_jump > 0:
   jump()
   numbers_of_jump -= 1
   print(numbers_of_jump)
for i in range(6):
   jump()

 # Hurdle =2
while at_goal() == False:
      jump()