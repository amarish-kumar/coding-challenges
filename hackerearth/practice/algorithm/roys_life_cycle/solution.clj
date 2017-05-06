(import '(java.io BufferedReader))


(defn count-c-streaks-in-day [day]                ; return C streaks in a given day

  (loop [chars day c-count 0 c-streaks []]

    (if (not= (count chars) 0)

      (if (= (first chars) \C)
        (recur (rest chars) (inc c-count) c-streaks)
        (recur (rest chars) 0 (if (not= c-count 0) (conj c-streaks c-count) c-streaks))
      )
      (if (not= c-count 0) (conj c-streaks c-count) c-streaks)          ; add the last C streak if day ended with C
    )
  )
)


(let [n (Integer/parseInt (read-line))
      d (line-seq (BufferedReader. *in*))]

  (apply println
    (loop [days d max-y 0 y 0 max-x 0]      ; y = streak across days

      (if (not= (count days) 0)

        (let [day (first days)                                          ; string of current day
              xs (count-c-streaks-in-day day)                           ; C streaks of current day
              cont-c (if (not= (first day) \C) 0 (first xs))            ; C streak to be added to last day's streak
              max-x-day (if (not= (count xs) 0) (apply max xs) 0)]      ; max C streak of the day

          (if (not= cont-c (count day))

            (recur (rest days)
                   (max max-x-day max-y (+ y cont-c))       ; max-y = max(current day's max streak, max-y, multi-day streak that ended today)
                   (if (= (last day) \C) (last xs) 0)       ; start a multi-day streak if last min of the day was C
                   (max max-x max-x-day)
            )

            (recur (rest days)                    ; if full day was a C streak, continue it
                   max-y
                   (+ y cont-c)
                   (max max-x max-x-day)
            ) 
          )
        ) [max-x (max y max-y)]                   ; if the last day was a full day C streak, update max-y
      )
    )
  )
)

