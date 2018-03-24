from die import Die
from walker import Walker

if __name__ == "__main__":
    w = Walker()
    w.fill_walk() 
    print("Walker Initial: " + str(w.num_points))
    w_memento = w.create_memento()
    w.set_memento(w_memento)
    print("Walker Final: " + str(w.num_points))
    
    d = Die()
    d.roll()
    print("Die Initial: " + str(d.num_sides))
    d_memento = d.create_memento()
    d.set_memento(d_memento)
    print("Die Final: " + str(d.num_sides))
    
