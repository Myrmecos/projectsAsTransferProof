import WorldMapper

if __name__ == "__main__":
    shp = np.array([100, 50])
    w = 10
    elevation = np.ones(shp)
    object = np.zeros(shp)
    def update_object(nurcle, object):
        object = np.minimum(signal.convolve2d(object, nurcle, 'same') + object, np.ones_like(object))
        return object
    def drawArray(object, nurcle):
        pg.init()
        screen = pg.display.set_mode(shp*(w + 1))
        wm = WorldMapper(elevation, object, screen, w)
        done = False
        while not done:
            for event in pg.event.get():  # User did something
                if event.type == pg.QUIT:  # If user clicked close
                    done = True
            print("one flip")
            screen.fill((0, 60, 0))
            wm.drawWorld("Grass")
            pg.display.flip()
            time.sleep(3)
            wm.object = update_object(nurcle, wm.object)
        pg.quit()

    from spicy import signal
    nurcle = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    nurcle = np.ones([10, 10])
    nur = ng.Nurcle(3, 1)
    nurcle = nur.matrix
    print(nurcle)
    #for i in [0, 1, 8, 9]:nurcle[0, i] = 0; nurcle[9, i] = 0
    #for i in [1, 8]: nurcle[i, 0] = nurcle[i, 9] = 0

    A = np.zeros(shp)
    B = np.zeros(shp)
    A[30, 30] = 1
    A[10, 5] = 1
    A[15, 6] = 1
    A[19, 9] = 1
    #A1 = signal.convolve2d(A, nurcle, 'same')
    #for i in range(1):
        #A1 = signal.convolve2d(A1, nurcle, 'same')

    drawArray(A, nurcle)













